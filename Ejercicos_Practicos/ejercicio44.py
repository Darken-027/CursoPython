'''
Ejercicio 44
generar un numero aleatorio entre 1 y 10,
luego, pide al usuario adivinar el numero
hasta que lo haga correctamente.

'''

import random
numero_secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input('Adivina el numero'))
    intentos = intentos + 1
    if intento == numero_secreto:
        print(f"Exito! tomo {intento} intentos")
        break