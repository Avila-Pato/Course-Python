# Ejemplo:
# Entrada: "hola mundo"
# Salida esperada (puedes imprimir el diccionario):
# {'h': 1, 'o': 2, 'l': 1, 'a': 1, ' ': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}


from collections import Counter

num = input("Ingrese una letra: ")
caracteres = Counter(list(num))
print(caracteres)

