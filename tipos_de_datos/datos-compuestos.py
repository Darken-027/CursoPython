#Los datos compuesto son datos que estan compuesto por otros datos y podemos agruparlos

#Matris o Lista son conjuntos de Datos
lista = ["David Ahstell","Soy Ahstell",True,1.70]
print(lista[0])

#Tupa son iguales a las listas pero no se pueden modificar
tupla = ("David Ahstell","Soy Ahstell",True,1.70)
print(tupla[0])

#Creando un conjunto
#Un conjunto es casi igual que una lista pero no se pueden modificar elementos
#Se puede reconstruir pero cada elemento no se puede modificar
#No podemos acceder por el indice a un elemento del conjunto
#No nos permite repetir valores
#Se puede iterar

conjunto = {"Ahstell Data", "Soy Ahstell", True, 1.60}
print(conjunto)

#Diccionario
diccionario = {
    'nombre' : "David Ahstell",
    'canal' : "Ahstel027",
    'estas_emocionado' : True,
    'altura' : 1.75
}

print(diccionario['canal'])
