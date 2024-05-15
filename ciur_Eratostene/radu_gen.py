from math import sqrt
from tqdm import tqdm


lista_numere = []


n = 1_000_000_0

for i in range(n+1):
    lista_numere.append(0)
    
for i in tqdm(range(2, int(sqrt(n)))):
    if lista_numere[i] != 1:
        for j in range(i*2, n+1, i):
            lista_numere[j] = 1
            
with open("eratos.txt", "w") as f:
    f.write(str(lista_numere))