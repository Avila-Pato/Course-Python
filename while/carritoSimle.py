# 1.- Agregar productos a la lista del súper
# 2.- Muestre mensaje indicado “Incorpore el valor del {producto}:”
# 3.- Agregue el valor del producto a la lista “valorSuper”
# 4.- Muestre mensaje indicando “----DETALLE BOLETA-----”
# 5.- Muestre mensaje indicando los productos comprados
# 6.- Muestre mensaje indicando la cantidad de productos comprados
# 7.- Muestre mensaje indicando la suma total de todos los productos
import os

if os.system("clear") !=0: os.system("cls")

valorSuper = []

while True:
    user  = input("Incorpore el valor del producto \n (salir) para terminar: ")
    if user == "salir":
        print("cerrendo..")
        exit()
    
    valorSuper.append(user)
    print(valorSuper)
