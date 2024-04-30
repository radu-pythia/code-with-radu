
def fibonacci_pana_la(numar):
    array = [0,1]
    numar_plus_1 = numar + 1 # Because number not included in range limit.
    for x in range(1, numar_plus_1):
            doi = 2
            suma_ultimelor_doua_din_array = sum(array[-doi:])
            print(suma_ultimelor_doua_din_array)
            array.append(suma_ultimelor_doua_din_array)

def fibonacci_pentru(numar):
    array = [0,1]
    numar_plus_1 = numar + 1 # Because number not included in range limit.
    for x in range(1, numar_plus_1):
            doi = 2
            suma_ultimelor_doua_din_array = sum(array[-doi:])
            if x == numar:
                  print(suma_ultimelor_doua_din_array)
                  break
            
            array.append(suma_ultimelor_doua_din_array)


print("Fibonacci pana la numarul zece:")
fibonacci_pana_la(12)
print("Fibonacci pentru numarul cinci:")
fibonacci_pentru(5)
