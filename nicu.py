# Verificam daca un numar este prim
n= int(input("Introduceti un numar: "))
x= True
for i in range(2,int(n/2)):
    if n%i==0:
        print(i, (" divide "), n)
        x= False
        break
if x==False:
    print(n, (" nu este numar prim"))
else:    
    print(n, (" este numar prim"))