import os

if os.system("clear") != 0:
    os.system("cls")


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


#   print(f"ID: {id}, Nombre: {nombre}, País: {pais}, Fecha: {fecha}")


def turistas_por_pais(pais):
    for id, dato in turistas.items():
        nombre = dato[0]
        pais = dato[1]
        mes = dato[2]
        if pais_busqueda.lower() == pais.lower():
            print(f" Nombre: {nombre}")

    if not pais_busqueda in pais:
        print("No hay turistas de ese pais")


def turistas_por_mes(mes_busqueda):
    while True:
        # Validar que el mes sea un número entre 1 y 12
        if not (mes_busqueda.isdigit() and 1 <= int(mes_busqueda) <= 12):
            print("Mes inválido. Intente nuevamente.")
            mes_busqueda = input("Ingrese mes a buscar (1-12): ")
            continue

        cantidad = 0

        for id, dato in turistas.items():
            fecha_turista = dato[2]  # Suponemos formato "dd-mm-aaaa"
            mes_turista = int(fecha_turista[3:5])

            if mes_turista == int(mes_busqueda):
                cantidad += 1
                print(f"ID: {id} | Fecha: {fecha_turista}")

        if cantidad == 0:
            print("No hay turistas en ese mes.")
        else:
            porcentaje = (cantidad / len(turistas)) * 100
            print(f"El porcentaje de turistas de ese mes es {porcentaje:.2f}%")

        break


def eliminar_turista(id_borrar):

    if id_borrar in turistas:
        datos = turistas[id_borrar]
        # Si es por ID   001, 002, 012
        print(
            f"Se eliminará el turista: ID: {id_borrar} | Nombre: {datos[0]} | País: {datos[1]} | Fecha: {datos[2]}"
        )
        confimacion = input("Desea confiamarlo ? (s/n)")
        if confimacion == "s":
            del turistas[id_borrar]
            print("Turista borrado")
        else:
            print("Eliminación cancelada.")
    else:
        print("Ingrese un valor valido")


def salir():
    print("Programa terminado...")


while True:
    menu()
    opc = input("Ingrese una opcion: ")
    match opc:
        case "1":
            pais_busqueda = input("Ingrese el Pais: ")
            turistas_por_pais(pais_busqueda)
        case "2":
            mes_busqueda = input("Ingrese mes a buscar: ")
            turistas_por_mes(mes_busqueda)
        case "3":
            id_borrar = input("Ingrese el ID del turista que desea eliminar: ")
            eliminar_turista(id_borrar)
        case "4":
            salir()
            break
        case _:
            print("Ingrese una opcion correcta")
