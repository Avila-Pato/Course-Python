import os 
if os.system("clear") !=0: os.system("cls")

lista1 = ['a', 'b', 'c', 'd']

lista1.append('e') # Agrega un elemento al final de la lista
print (lista1)

lista1.insert(2, 'x') # Inserta un elemento en una posició especifica
print (lista1)

lista1.remove('a') # Elimina un elemento de la lista
print (lista1)

lista1.pop() # Elimina el ultimo elemento de la lista
print (lista1)

lista1.clear() # Elimina todos los elementos de la lista
print (lista1)

lista1.extend(['f', 'g', 'h']) # Agrega varios elementos al final de la lista
print (lista1)

lista1.sort() # Ordena los elementos de la lista
print (lista1)

lista1.reverse() # Invierte la lista
print (lista1)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False


###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# 1. Crea una lista con los números del 1 al 10 y luego elimina el número 5 de la lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.remove(5)
print(numeros)
# crea una lista del 1 al 5 y añade el 6 al final de la lista
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)
# inseta un numero 10 en la posicion2 de lalista 
numeros.insert(2, 10) ## insertar en la posicion 2 el numero 10
print(numeros)
# modificar el primer elemetno
numeros[0] = 0 # Cambia el primer elemento de la lista por 0
print(numeros)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

extendiendo = lista_a.extend(lista_b) # Extiende la lista_a con los elementos de lista_b
print(extendiendo) # Imprime la lista_a extendida

#Elimina la primera apaciiond el numero 1 en la lisata_a usando remove()

lista_a.remove(1) # Elimina el primer elemento 1 de la lista_a
print(lista_a) # Imprime la lista_a después de eliminar el 1

#crea una lista con los numeros del 1 al 10
# utiliza slicing y del para eliminar los elementos desde el indice 2 hasta el 5
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros[2:5] = [] # Elimina los elementos desde el índice 2 hasta el 5
print(numeros)

#Copia vs referencia
#crea una lista del 1 al 3
# crea una copia de la lsita original llamada copia_1 usando slicing
#crea otra copia llamada copia_2 usando el metodo copy()
# crea una referencia a la lista original llamada refecencia
#modifica el primer elemento de la lista referencia a 10
#imprime las cuatro listas originales

numeros = [1, 2, 3]
copia_1 = numeros[:] # Copia la lista usando slicing
copia_2 = numeros.copy() # Copia la lista usando el método copy()
referencia = numeros # Crea una referencia a la lista original
referencia[0] = 10 # Modifica el primer elemento de la lista original

print(numeros) # Imprime la lista original

## ordenar la lista sin diferencia de mayusculas y minusculas
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lista.sort() # Ordena la lista sin diferencia de mayusculas y minusculas

listaFruts = ['Manfico', 'banana', 'Aguatate', 'naranja']
listaFruts.sort(key=str.lower) # Ordena la lista sin diferencia de mayusculas y minusculas
print(listaFruts) # Imprime la lista ordenada sin diferencia de mayusculas y minusculas