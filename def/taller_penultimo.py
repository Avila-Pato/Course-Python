import os

if os.system("clear") !=0: os.system("cls")

turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}


def menu():
    print("*** MENU PRINCIPAL ***")
    print("1) Turista por pais ")
    print("2) Turista por mes ")
    print("3) Eliminar turista ")
    print("4) Salir")
    
def turistas_por_pais():
    buscar_pais  = input("Ingrese el Pais: ")
    
    for id, datos in turistas.items():
        nombre = datos[0]
        pais = datos[1]
        fecha = datos[2]
        if pais.lower() == buscar_pais.lower():
            print(f"ID: {id} | Nombre: {nombre} | País: {pais} | Fecha: {fecha}")
    else:
        print("No hay turista de ese pais ")
        
def turistas_por_mes():
    
    while True:
        
        mes = input("Ingrese mes a buscar: ")
        
        
        if not (mes.isdigit() and 1 <= int(mes) <= 12):
            print("Mes inválido. Intente nuevamente.")
            continue

        contador = 0
        
        for id, datos in turistas.items():
            fecha = datos[2]
            # la fecha esta en formato dd-mm-aaaa
            if  fecha[3:5] == mes:
                contador += 1
                print(f"ID: {id} | Fecha: {fecha}")

        if contador == 0:
            print("No hay turistas de ese mes")
        
        else:
            porcentaje = (contador / len(turistas)) * 100
            print(f"Porcentaje de turistas en el mes {porcentaje:.2f}%")
            
        break
        
def eliminar_turista():
    id_borrar = input("Ingrese el ID del turista que desea eliminar: ").strip()
    
    if id_borrar in turistas:
        datos = turistas[id_borrar]
        print(f"Se eliminará el turista: ID: {id_borrar} | Nombre: {datos[0]} | País: {datos[1]} | Fecha: {datos[2]}")
        confirmacion = input("¿Está seguro? (s/n): ").strip().lower()
        if confirmacion == "s":
            del turistas[id_borrar]
            print("Turista eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print("No existe un turista con ese ID.")

    
def salir():
    print("Saliendo...")
    

while True:
    menu()
    opc = input("Ingrese una opcion ")
    
    match opc:
        case "1":
            turistas_por_pais()
        case "2" :
            turistas_por_mes()
        case "3":
            eliminar_turista()
        case "4":
            salir()
            break
        case _:
            print("Ingrese una opcion valida")