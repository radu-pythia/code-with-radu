from matplotlib import pyplot as plt
# print("Hello world!")


n= int(input("Introduceti un numar: "))
print("Secventa Fibonacci")
lista=[1,1]
x = [_ for _ in range(n)]
for f in range(2,n):
    lista.append(lista[f-1]+lista[f-2])
# print(lista)


# # 

# Accesare --  lista[n] 
# Appending -- lista.append(x)

print(lista[n-1])

plt.plot(x, lista)

plt.savefig(f"fibonacci {n}")

