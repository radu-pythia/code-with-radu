# Se creeaza "ciurul" lui Eratostene cu ajutorul ALGORITMULUI lui Eratostene
import math
n= int(input("Introduceti un numar: "))
lista=[]
lista_i=[]
for i in range(n+1):
    lista.append(0)
    lista_i.append(i)
for i in range(2,int(math.sqrt(n))+1):
    for j in range(2,int(n/2)+1):
        if i*j>n:
            break
        print(i,(", "),j)
        lista[i*j]=1
print(int(math.sqrt(n)))
print(lista_i)
print(lista)