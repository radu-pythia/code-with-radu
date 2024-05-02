
def fibonacci_pana_la(numar):
    array = [1,1]
    numar_plus_1 = numar + 1 # Because number not included in range limit.
    print("1")
    for x in range(2, numar):
        if numar == 1:
            break
        doi = 2
        suma_ultimelor_doua_din_array = sum(array[-doi:])
        # suma_ultimelor_doua_din_array = array[x-1]+array[x-2]
        
        print(suma_ultimelor_doua_din_array)
        array.append(suma_ultimelor_doua_din_array)
            
  

def fibonacci_pentru(numar):

    array = [1,1]
    for x in range(2, numar):
            doi = 2
            suma_ultimelor_doua_din_array = sum(array[-doi:]) 
            array.append(suma_ultimelor_doua_din_array)
    print(suma_ultimelor_doua_din_array)


print("Fibonacci pana la numarul 200:")
fibonacci_pana_la(10)
print("Fibonacci pentru numarul 100:")
fibonacci_pentru(10)
