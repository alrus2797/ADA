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
     



##Generar listas            
'''for i in range(0,5000):
    print(generator(i))
'''

            
##correr algoritmo con data
'''

for i in range(0,2930):
    a=ast.literal_eval(input())
    start=time.time()
    insert(a)
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


insertar=open('insertout.txt','r')
insertarl=[]
insertart=[]
for i in insertar.readlines():
    a=ast.literal_eval(i)
    insertarl.append(a[0])
    insertart.append(a[1])

mergear=open('mergeout.txt','r')
mergearl=[]
mergeart=[]
for i in mergear.readlines():
    a=ast.literal_eval(i)
    mergearl.append(a[0])
    mergeart.append(a[1])



#plt.plot(bublearl,bubleart,"g")
plt.plot(mergearl,mergeart,"b")
plt.plot(insertarl,insertart,"r")
plt.ylabel("Tiempo")
plt.xlabel("Tamaño")

red_patch = mpatches.Patch(color='blue', label='Merge sort')
#green_patch = mpatches.Patch(color='green', label='Bubble sort')
blue_patch = mpatches.Patch(color='red', label='Insert sort')
plt.legend(handles=[blue_patch,red_patch])


plt.show()

