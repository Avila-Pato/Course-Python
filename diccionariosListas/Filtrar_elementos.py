# Ejemplo:
#  Crea un diccionario nuevo que contenga solo los pares cuya clave empiece con una vocal.
dic = {'ana': 1, 'luis': 2, 'oso': 3, 'pato': 4}
# Salida esperada:
# {'ana': 1, 'oso': 3}

# dic.items() devuelve un iterable de pares(clave, valor del diccionario)
# {clave: valor for clave, valor in dic.items() if clave[0] in 'aeiou'} esto es un dic comprehension
# Crea un nuevo diccionario con los pares (clave, valor), pero solo si la clave cumple la condición.
#clave[0] toma el primer caracter de la clave in "aeiou"
filtrados = {clave: valor for clave, valor in dic.items() if clave[0].lower() in 'aeiou'}
print(filtrados)


productos = {'manzana': 500, 'pan': 1200, 'leche': 1500, 'agua': 700}
filtradoProductos = {clave: valor for clave, valor in productos.items() if valor > 1000}
print(filtradoProductos)

