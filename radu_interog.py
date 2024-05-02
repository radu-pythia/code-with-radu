from tqdm import tqdm

lista_numere = [] 
with open("eratos.txt", "r") as f:
     tmp = f.read()

for ch in tqdm(tmp):
    if ch in ["[","]"," ",","]:
        continue
    lista_numere.append(int(ch)) 

stop = False
while not stop:
    check = input("verifica daca e prim")
    if check == "s":
        stop = True
        break
    else: 
        check = int(check)
    if lista_numere[check]:
        print("nu e prim")
    else:
        print("ii prim")