
 

# Enunciado 1: Gestión de Tareas Pendientes 

# Descripción: Este sistema permite al usuario gestionar una lista de tareas pendientes. Cada tarea tendrá un nombre y un estado (pendiente/completada). Se podrán añadir, ver, marcar como completada y eliminar tareas. 

# Características Clave: 

# •	Uso de una lista de diccionarios para almacenar las tareas. 

# •	Menú interactivo. 

# •	Funciones separadas para cada operación (añadir, ver, modificar, eliminar). 

# •	Control de errores para entradas inválidas y tareas no encontradas. 

# •	Ciclos while para el menú principal y for para iterar sobre las tareas. 

# •	Decisiones if/elif/else para la lógica del menú y las operaciones. 

tareas = []

def mostrar_menu():
    print("***MENU**")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Modificar Tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def Añadir():
    print("1. Matematica")
    print("2. Biologia")
    print("3. Lenguaje")
    
    while True:
        asignaturas = input("Ingrese el módulo (1-Mate, 2-Bio, 3-Leng): ")
        tarea = {"Matematicas": "", "Biologia": "", "Lenguaje": ""}

        match asignaturas:
            case "1":
                tarea["Matematicas"] = input("Ingrese la tarea de Matemáticas: ")
            case "2":
                tarea["Biologia"] = input("Ingrese la tarea de Biología: ")
            case "3":
                tarea["Lenguaje"] = input("Ingrese la tarea de Lenguaje: ")
            case _:
                print("Ingrese una opción correcta")

        print("Tarea ingresada con éxito.")
        tareas.append(tarea)
        break  
    
def Ver_Tarea():
            # if len(tareas) == 0:
            #         print("No hay tareas aqui")
            #         return
    name = input("Ingrese la asignatura a ver (1-Mate, 2-Bio, 3-Leng): ")
    if not tareas:
        print("No hay tareas registradas")
        return
    tiene_tarea = False 
    if name == "1":
        for i, tarea in enumerate(tareas):
            if tarea["Matematicas"]:
                print(f"\nTarea #{i+1}")
                print("Matemáticas:", tarea["Matematicas"])
                tiene_tarea = True
        if not tiene_tarea:
            print("No hay tareas en Matemáticas")
    elif name == "2":
        for i, tarea in enumerate(tareas):
            if tarea["Biologia"]:
                print(f"\nTarea #{i+1}")
                print("Biología:", tarea["Biologia"])
                tiene_tarea = True
        if not tiene_tarea:
            print("No hay tareas en Biología")
    elif name == "3":
        for i, tarea in enumerate(tareas):
            if tarea["Lenguaje"]:
                print(f"\nTarea #{i+1}")
                print("Lenguaje:", tarea["Lenguaje"])
                tiene_tarea = True
        if not tiene_tarea:
            print("No hay tareas en Lenguaje")
    else:
        print("Ingrese una opción correcta")

def Modificar_tarea():
    if not tareas:
        print("No hay tareas registradas")
        return

    print("## Lista de tareas ##")
    tiene_tarea = False
    for i, t in enumerate(tareas):
        if t["Matematicas"] or t["Biologia"] or t["Lenguaje"]:
            print(f"\nTarea id#{i+1}")
            for materia, contenido in t.items():
                if contenido.strip():
                    print(f"{materia}: {contenido}")
            tiene_tarea = True
    if not tiene_tarea:
        print("## No hay tareas con contenido ##")
        return

    try:
        id_tarea = int(input("\nIngrese el id de la tarea que desea modificar: ")) - 1
        if 0 <= id_tarea < len(tareas):
            tarea_seleccionada = tareas[id_tarea]

            materias_con_datos = {k: v for k, v in tarea_seleccionada.items() if v.strip()}
            if not materias_con_datos:
                print("La tarea seleccionada no contiene información.")
                return

            if len(materias_con_datos) == 1:
                materia = list(materias_con_datos.keys())[0]
                nueva_tarea = input(f"Ingrese la nueva tarea para {materia}: ")
                tarea_seleccionada[materia] = nueva_tarea
                print("Tarea modificada con éxito.")
            else:
                print("\nMaterias disponibles para modificar:")
                for idx, (materia, contenido) in enumerate(materias_con_datos.items(), 1):
                    print(f"{idx}. {materia}: {contenido}")

                opcion = int(input("Seleccione el número de la materia que desea modificar: ")) - 1
                materia = list(materias_con_datos.keys())[opcion]
                nueva_tarea = input(f"Ingrese la nueva tarea para {materia}: ")
                tarea_seleccionada[materia] = nueva_tarea
                print("Tarea modificada con éxito.")
        else:
            print("ID de tarea inválido.")
    except ValueError:
        print(" Entrada inválida. Debes ingresar un número.")
    except IndexError:
        print("Selección fuera de rango.")

def Eliminar_tarea():
    if not tareas:
        print(" No hay tareas registradas.")
        return

    print("## Lista de tareas con contenido ##")
    tareas_con_datos = []

    for i, t in enumerate(tareas):
        if any(valor.strip() for valor in t.values()):
            print(f"\nTarea id#{i+1}")
            for materia, contenido in t.items():
                if contenido.strip():
                    print(f"{materia}: {contenido}")
            tareas_con_datos.append(i)

    if not tareas_con_datos:
        print("No hay tareas con contenido.")
        return

    try:
        id_tarea = int(input("\nIngrese el ID de la tarea que desea eliminar: ")) - 1
        if id_tarea not in tareas_con_datos:
            print("ID inválido o tarea vacía.")
            return

        print("\n¿Se elimina toda la tarea? Confirmar")
        opcion = input("Selecciona (s/n): ")

        if opcion.lower() == "s":
            tareas.pop(id_tarea)
            print("Tarea eliminada completamente.")
        else:
            print("Eliminación cancelada.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")
    except IndexError:
        print("Selección fuera de rango.")

        
def salir():
    print("Saliendo....")

while True:
    mostrar_menu()
    opc = input("Ingrese una opcion ")
    
    match opc:
        case "1":
            Añadir()
        case "2":
            Ver_Tarea()
        case "3":
            Modificar_tarea()
        case "4":
            Eliminar_tarea()
        case "5":
            salir()
            break
        case _:
            print("Ingrese una opcion correcta ")       
            
    

 
