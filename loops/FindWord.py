
import os 

if os.system("clear") != 0: os.system("cls")

find_word = input("Escriba un nombre \n")

contador = 0
for letra in find_word:
    if letra.lower() == 'a' and 'A':
        contador += 1
print(f'La palabra a sido encontrada {contador} Veces ' )



#Otra forma de buscar una letra usando el metodo Find()

# txt = "Hello, welcome to my world."
# x = txt.find("e")
# print(x)