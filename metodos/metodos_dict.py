diccionario = {
    "nombre" : 'lucas',
    "apellido" : 'Junner',
    "subs" : 10000000
}

#nos devuelve un objeto dict_item
clave = diccionario.keys()

#obteniendo un elemento con get() si no encuentra nada el programa continua
clave = diccionario.get("lucas")
print("Hola papa")

print(clave)