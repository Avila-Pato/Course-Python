

lista_numeros = []
def menu():
    print("1)ingresar un número entero entre 0 y 100")
    print("2)mostrar el número mayor ingresado")
    print("3)mostrar el número menor ingresado")
    print("4)Terminar programa")
    
def ingresar_numero():
    
    num = int(input("Ingrese un numero"))
    if num <= 100:
        print("Numero Ingresado Correctamente")
        lista_numeros.append(num)
    elif num > 100:
        print("Ingrese un numero menor a 100")
    else:
        print("Ingrese un valor valido")
        
def mostrar_mayor():
    numero_mayor = max(lista_numeros)
    print(f"El numero mayor de la lista es {numero_mayor}")

def mostrar_menor():
    numero_menor = min(lista_numeros)
    print(f"El numero menor de la lista es {numero_menor}")
    
def salir():
    print("Saliendo..")
    
while True:
    menu()
    
    try:
        opc = int(input("Elija 1 opcion: "))
        
        match opc:
            case 1:
                ingresar_numero()
            case 2:
                mostrar_mayor()
            case 3:
                mostrar_menor()
            case 4:
                salir() 
                break
            case _:
                print("Ingrese un numero de la lista")       
        
    except:
        print("Ingrese un valor valido")