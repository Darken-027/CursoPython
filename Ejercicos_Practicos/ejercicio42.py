'''
Ejercicio 42
Solicita al usuario un numero N y luego
imprime la suma de todos los numeros
desde 1 hasta N

'''

numero = int(input('Ingresa un numero'))
suma = 0
i = 1

while i <= numero:
    suma += i
    i += 1
print('La suma es', suma)