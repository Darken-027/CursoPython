'''
Ejercicio 49
simular un lanzamiento
de un dado hasta obtener un 6

'''

import random
numero = 0
while numero != 6:
    numero = random.randint(1, 2)
    print(f"Has sacado un { numero }")
    
print("Sacaste un 6")