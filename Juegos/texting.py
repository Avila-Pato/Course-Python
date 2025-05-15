import random

cadena  = ["cerdo", "loro", "ballena", "langosta"]

progreso = [["_"] * len(cadena) for palabra in cadena]

indice_random = random.randint(0,  len(cadena) - 1)

palabra_seleccionada = cadena[indice_random]  
progrese_seleccionado = progreso[indice_random]

print(palabra_seleccionada)
print(progrese_seleccionado)