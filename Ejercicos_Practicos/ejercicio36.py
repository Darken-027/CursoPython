'''
Ejercicio 36
pide un caracter y comprueva si 
es una vocal

'''

caracter = input("Ingresa el caracter")
vocales = ['a', 'e', 'i', 'o', 'u']

if caracter.lower() in vocales:
    print("Es una vocal")
else:
    print("No es una vocal")