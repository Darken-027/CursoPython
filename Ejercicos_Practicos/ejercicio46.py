'''
Ejercicio 46
solicita al usuario ingresar 
un numero y cuenta cuantos digitos tiene

'''

numero = int(input('Ingresa el numero'))
contador = 0
while numero != 0:
    numero = numero // 10
    contador = contador + 1
print("Digitos son " , contador)