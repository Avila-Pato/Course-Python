import os 
if os.system("clear") != 0: os.system("cls")

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print(mensaje[7])
# print(mensaje[7:]) // Imprime desde el índice 7 hasta el final

numeros = [1, 2, 3, 4, 5]
numeros[0], numeros[4] = numeros[4], numeros[0] # Intercambia el primer y último elemento
print(numeros)

pan = ["Pan arriba"]
ingredietnes = ["Jamon", "Queso", "Lechuga", "Tomate"]
pan_abajo = ["Pan abajo"]
sandwich = pan + ingredietnes + pan_abajo
print(sandwich)

lista = [1, 2, 3, 4, 5]
lista_duplicada = lista * 2 # Duplica la lista
print(lista_duplicada)

lista = [1, 2, 3, 4, 5]
centro = len(lista) // 2 # Encuentra el índice del centro
print(centro)

lista = [1, 2, 3, 4, 5]
mitad = len(lista) // 2 # Encuentra el índice de la mitad
lista_invertida = lista[mitad:] + lista[mitad:] # Invierte la lista
print(lista_invertida) 


