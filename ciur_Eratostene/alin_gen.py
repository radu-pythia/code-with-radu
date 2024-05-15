primes = []

max = int(input("pana unde? "))

def ii_prim(n):
    for j in range(2, int(n/2)+1):
        if n % j == 0:
            return False
    return True
    
    

for i in range(1, max+1):
    if ii_prim(i):
        primes.append(i)
        
with open("prime.txt", "w") as f:
    f.write(str(primes))

    
