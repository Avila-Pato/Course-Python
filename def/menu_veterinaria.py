
clientes = []
hora_agendada = []

def menu():
    print("1) Agregar mascota ")
    print("2) Listar  Mascota")
    print("3) Buscar mascota ")
    print("4) Borrar mascota")
    print("5) Agendar Hora ")
    print("6) Salir ")
    

def nombre():
    
    try:
        name = input("Ingrese su nombre ")
        mascota = input("Ingrese el nombbre del animal ")
    except:
        print("error ingrese un nombre valido")    
    
    dicccionario = {
        "Nombre dueño": name,
        "Nombre mascota": mascota
    }

    clientes.append(dicccionario)
    
    print("Agregados Correctamente ")
    
def listado():
    for i, cliente in enumerate(clientes, 1):
        print({f"Id {i}"})
        print(f"Nombre Cliente {cliente["Nombre dueño"]}",  )
        print(f"Nombre Mascota {cliente["Nombre mascota"]}")
        
def buscarMascota():
        name = input("Ingrese el nombre de la mascota")
        
        if name in clientes:
            print("El aninmal", name, " Se encuentra en la lista")
        else:
            print("No encontrado")
def borrarMascota():
    name = input("Ingrese el nombre del dueño que desea borrar: ")
    
    for cliene in clientes:
        if cliene["Nombre dueño"] == name.lower():
            clientes.remove(cliene)
        print("Cliente eliminado ")
def agendarHora():
    try:
        hora = int(input("Ingrese la hora que desea agendar: "))
        
        horaCliente = {
            "Hora": hora
        }
        
        hora_agendada.append(horaCliente)
        print("Hora agregada correctamente")
        
        for i, h in enumerate(hora_agendada, 1):
            print(F"id {i}")
            print(f"Hora {h["Hora"]}")
            
        
        
        
    except:
        print("Ingrese una hora validad ")
        
def salir():
    print("Saliendo...")
while True:
    menu()
    
    try:
        opc = input("Ingrese una opcion ")
        
        match opc:
            case "1":
                nombre()
            case "2":
                listado()
            case "3":
                buscarMascota()
            case "4":
                borrarMascota()   
            case "5":
                agendarHora() 
            case "6":
                salir()  
                break
            case _:
                print("Ingrese una opcion valida")
    except:
        print("Ingrese una opcion valida ")  