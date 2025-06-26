import os

if os.system("clear") !=0: os.system("cls")

clientes = []

def menu():
    print("**Menu**")
    print("1- Ingresar usuario ")
    print("2- Buscar usuario ")
    print("3- Eliminar Usuario ")
    print("4- Salir")


def ingrese_usuario():
    name = input("Ingrese el nombre de usuario: ")
    
    flag = True
    while flag:
        
        gender = input("Ingrese el sexo: ").lower()
        if gender not in("f", "m"):
            print("Debe ingresar M o F solamente. Intente de nuevo. ")
        else:
            print("Sexo confirmado")
            flag = False

            flag2 = True
            while flag2:             
                password = input("Ingrese contraseña: ") 
                if  not any (char.isdigit() for char in password):
                    print("Contraseña no válida: debe contener al menos un número. ")
                if not any (char.isupper() for char in password):
                    print("Debe tener al menor una letra mayuscula")
                if len(password) < 4:
                    print("debe tener al menor 4 caracteres ")
                else:
                    flag2 = False
                    print("Usuario ingresado con exito !! ")    
                
    usuario = {
        "Name": name,
        "Gender": gender,
        "Paswword": password
    }            
    
    clientes.append(usuario)
        

def buscar_usario():
    name = input("Ingrese el nombre del usuario a buscar: ")
    encontrado = False
    for cliente in clientes:
        if  cliente["Name"] == name.lower():
            print(f"Cliente {cliente["Name"]}, Genero, {cliente["Gender"]}, Password {cliente["Paswword"]}")
            encontrado = True
        else:
            print("Ingrese una opcion corretaas")
        
    if not encontrado:
        print("Usuario no encontrado")    
        
            
def eliminar_usuario():
    name = input("Ingrese el usuario a buscar ")
    
    for cliente in clientes:
        if name == cliente["Name"]:
             print(f"Cliente {cliente["Name"] }")
             confirmacion = input("Desea boorrarlo ? (s/n)").lower()
             
             if confirmacion == "s":
                 clientes.remove(cliente)
                 print("Borrado corectamente")
             else:
                 print("Usuario no borrado")
    
def salir():
    print("Terminando programa...")
    


while True:
    menu()
    opc = input("Ingrese una opcion: ")    
    

    match opc:
        case "1":
            ingrese_usuario()
        case "2":
            buscar_usario()
        case "3":
            eliminar_usuario()
        case "4":
            salir()
            break
        case _:
            print("Ingrese una opcion correcta ")
    
