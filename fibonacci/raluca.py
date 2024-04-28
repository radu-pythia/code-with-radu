print("nada")
lista=[]
i=2
lista.append(1)
lista.append(1)
n = int(input("lalala = "))
while i < n:
    lista.append(lista[i-1]+lista[i-2])
    print(lista[i])
    i= i+1
    