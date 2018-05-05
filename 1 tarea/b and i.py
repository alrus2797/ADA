import time
import random
import ast
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def insert(lista):
    ordenados=[float('-inf')]
    #lista=[float('inf')]+lista
    while len(lista)>=1:
        j=len(ordenados)-1
        #print(lista,ordenados,j)
        num=lista[0]
        while num<ordenados[j]:
            j-=1
        #print(j)
        ordenados.insert(j+1,num)
        del lista[0]
    return ordenados[1:]

def insertMerge(lista):
    ordenados=[float('-inf')]
    lista1=lista[1:]
    #lista=[float('inf')]+lista
    while len(lista1)>=1:
        j=len(ordenados)-1
        #print(lista,ordenados,j)
        num=lista1[0]
        while num<ordenados[j]:
            j-=1
        #print(j)
        ordenados.insert(j+1,num)
        del lista1[0]
    return [0]+ordenados[1:]
    print("insert",lista)


def insert1(lista):
    n=len(lista)
    lista=[float('-inf')]+lista
    i=2
    while i<n+1:
        #print(lista)
        j=i-1
        num=lista[i]
        while lista[i] < lista[j] and j>=0:
            j-=1
        del lista[i]
        lista.insert(j+1,num)
        i+=1
    return lista
        

def unir(l0,l1):
    res=[]
    while len(l0) >0 and len(l1)>0:
        if l0[0] <= l1[0]:
            res.append(l0[0])
            l0=l0[1:]
        else:
            res.append(l1[0])
            l1=l1[1:]
    if len(l0)>0:
        res=res+l0
    if len(l1)>0:
        res=res+l1
    return res
        


def merge(lista):
    if len (lista)<=1:
        return lista
    l0 = merge(lista[:len(lista)//2])
    l1 = merge(lista[len(lista)//2:])

    if l0[len(l0)-1] <= l1[0]:
        l0 = l0 + l1
        return l0
    res = unir(l0,l1)
    return res


def merge_hibrido_insert(lista):
    if len(lista)<64:
        return insert(lista)
    else:
        if len (lista)<=1:
            return lista
        l0 = merge(lista[:len(lista)//2])
        l1 = merge(lista[len(lista)//2:])

        if l0[len(l0)-1] <= l1[0]:
            l0 = l0 + l1
            return l0
        res = unir(l0,l1)
        return res
def merge_ver(lista):

    if len (lista)<=1:
        return lista
    l0 = merge(lista[:len(lista)//2])
    l1 = merge(lista[len(lista)//2:])
    if l0[len(l0)-1] <= l1[0]:
        l0 = l0 + l1
        return l0
    res = unir(l0,l1)
    return res

def merge_hibrido_quick(lista):
    if len(lista)<64:
        lista.sort()
        return lista
    else:
        if len (lista)<=1:
            return lista
        l0 = merge(lista[:len(lista)//2])
        l1 = merge(lista[len(lista)//2:])

        if l0[len(l0)-1] <= l1[0]:
            l0 = l0 + l1
            return l0
        res = unir(l0,l1)
        return res


def intercala(lista,p,q,r):
    b=lista[0:p]+lista[p:q+1]+lista[q+1:r+1][::-1]
    i=p
    j=r
    #print("intercala: ",b,i,j)
    #input("debug: ")
    for k in range(p,r+1):
        if b[i]<=b[j]:
            lista[k]=b[i]
            i+=1
        else:
            lista[k]=b[j]
            j-=1

a=[10,35,38,60,25,40,45,50,65,77,99]
a=[-1,20,25,35,40,44,50,10,38,55,65,99]
a=[00,55,33,66,44,99,11,77,22,88]
#intercala(a,1,6,11)
def insert_b(lista,n):
    n=n+1
    for j in range(2,n):
        clav=lista[j]
        i=j-1
        while(i>=1 and lista[i]>clav):
            lista[i+1]= lista[i]
            i-=1
        lista[i+1]=clav
#insert_b(a,9)
#print(a)
def merge_b(lista,p,r):
    if (r-p)<64:
        insert_b(lista,r-p+1)
    else:    
        if p<r:
            q=(p+r)//2
            #print(lista[p:r+1],lista[q],p,r)
            #input("debug merge:")
            merge_b(lista,p,q)
            #input("debug merge sec:"+str(q)+" "+str(r))
            merge_b(lista,q+1,r)
            intercala(lista,p,q,r)
a=[0,73, 70, 23, 83, 37]
merge_b(a,1,5)
print(a)
input()




def buble(lista):
    n=len(lista)+1
    for i in range(2,n):
        for j in range(0,n-i):
            if lista[j]>lista[j+1]:
                a=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=a
    return lista


def generator(n):
    res=[]
    for i in range(n):
        res.append(random.randint(0,100))
    return res

#a=[6,5,2,4,3,1,9,8,7]
#print(merge_hibrido_insert([]))



##Generar listas            
'''for i in range(0,5000):
    print(generator(i))
'''

            
##correr algoritmo con data

'''
for i in range(0,2929):
    a=[0]+ast.literal_eval(input())
    start=time.time()
    merge_b(a,1,i)
    #print(a)
    end=time.time()
    print([i,end-start])

'''

##Graficar

'''
bublear=open('bubleout.txt','r')
bublearl=[]
bubleart=[]
for i in bublear.readlines():
    a=ast.literal_eval(i)
    bublearl.append(a[0])
    bubleart.append(a[1])
'''
'''

insertar=open('insertout.txt','r')
insertarl=[]
insertart=[]
for i in insertar.readlines():
    a=ast.literal_eval(i)
    insertarl.append(a[0])
    insertart.append(a[1])
'''


mergear=open('mergeHIout.txt','r')
mergearl=[]
mergeart=[]
for i in mergear.readlines():
    a=ast.literal_eval(i)
    mergearl.append(a[0])
    mergeart.append(a[1])

mergehar=open('mergeHQout.txt','r')
mergeharl=[]
mergehart=[]
for i in mergehar.readlines():
    a=ast.literal_eval(i)
    mergeharl.append(a[0])
    mergehart.append(a[1])



#plt.plot(bublearl,bubleart,"g")
plt.plot(mergearl,mergeart,"b")
plt.plot(mergeharl,mergehart,"r")
plt.ylabel("Tiempo")
plt.xlabel("Tamaño")

red_patch = mpatches.Patch(color='blue', label='Merge Hibrido - Insert sort')
#green_patch = mpatches.Patch(color='green', label='Bubble sort')
blue_patch = mpatches.Patch(color='red', label='Merge Hibrido - Quick sort')
plt.legend(handles=[blue_patch,red_patch])


plt.show()
