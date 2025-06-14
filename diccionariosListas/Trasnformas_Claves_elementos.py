
# Cambiar las claves o valores al crear un nuevo diccionario.
numeros = {'uno': 1, 'dos': 2, 'tres': 3}

nuevo_valor = {clave: valor**2 for clave, valor in numeros.items()}
print(nuevo_valor)