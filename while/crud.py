
import os 

if os.system("clear") !=0: os.system("cls") 

lista = []

while True:
    opc = int(input("\n1)Ingrese un nombre\n2)Listar nombres\n3)borrar nombre\n4)nmodificar nombre\n5)Sali \n"))

    if opc == 1:
        nombre = str(input("\nIngrese el nombre:  "))
        lista.append(nombre)
        print("Nombre agreagado")
    elif opc == 2:
         for e in lista:
            print(f"Nombre: {e}")
    elif opc == 3:
        borrar = input("ingrese el nombre que desea borrar")
        lista.remove(borrar)
        print("Nombre Borrado")
    elif opc == 4:
        sub_name = input("Ingrese el nombre que desea modificar ")
        
        if sub_name in lista:
            nuevo_nombre = input("Ingrese el neuvo nombre ")
            indice = lista.index(sub_name) ## buscar el indice del nombreexistente para modificar
            lista[indice] = nuevo_nombre
            print(lista)
        else:
            print("el nombre no se encuentra en la lista")