from  collections import Counter

texto = input("Escribe una frase: ")

palabras = texto.split()
contador = Counter(palabras)
# contador = Counter(texto)
total = sum(contador.values())


#  values() en Python es un método que se utiliza con los diccionarios (dict) y sirve para obtener todos los valores (sin las claves) almacenados en ese diccionario
# ejemplo
# persona = {
#     "nombre": "Patricio",
#     "edad": 26,
#     "ciudad": "Santiago"
# }

# valores = persona.values()
# print(valores)  # dict_values(['Patricio', 26, 'Santiago'])

# # Si quieres una lista:
# print(list(valores))  # ['Patricio', 26, 'Santiago']
# #

print(list(contador))
print(F"Total de palabras: {total}") 