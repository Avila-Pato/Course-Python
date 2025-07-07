
# Enunciado 3: Registro de Estudiantes y Notas 

# Descripción: Este sistema permite registrar estudiantes y sus notas en diferentes asignaturas. Cada estudiante tendrá un nombre, una matrícula única y una lista de notas. 

# Características Clave: 

# •	Uso de un diccionario donde las claves son las matrículas de los estudiantes y los valores son diccionarios con el nombre y una lista de notas. 

# •	Funciones para añadir estudiantes, añadir notas, consultar notas, calcular promedios y eliminar estudiantes. 

# •	Control de errores para matrículas duplicadas, notas inválidas y estudiantes no encontrados. 

# •	Ciclos para el menú y para procesar las notas. 

 

estudiantes = {}

# estudiantes = {
#     "2025001": {
#         "nombre": "Ana",
#         "asignaturas": {
#             "Matemáticas": [6.0, 7.0],
#             "Historia": [5.5]
#         }
#     }
# }

 
def Menu():
    print("1- Agregar Estudiante")
    print("2- Consultar Estudiante")
    print("3- Calcular Promedio")
    print("4- Eliminar Estudiante")
    print("5- Salir")
    
def Agregar_estudiante():
    # matricula = input("Ingrese al amtricula del estudiante: ")
    # nombre = input("Ingrese el nombre dele estudiante: ")
    # notas = list(map(float, input("Ingrese las notas separadas por coma").split(",")))
    
    # estudiantes[matricula] = {
    #     'nombre': nombre,
    #     'notas': notas
    # }
    
    
    matricula = input("Ingrese la matrícula del estudiante: ")
    
    if matricula in estudiantes:
        print("Ya existe ese estudiante cone s matricula")
        return
    nombre = input("Ingrese el nombre del estudiante: ")
    asignaturas = {}
    
    while True:
        asignatura = input("Nombre de la asignatura o escriba 'fin' para terminare: ")
        if asignatura.lower() == 'fin':
            break
        
        try:
            notas = list(map(float, input("Ingrese las notas separadas por coma: ").split(",")))
            asignaturas[asignatura] = notas ##se cre aun nuevo diccionario que alamcena las notas de las asignaturas estas se pasan al diccionario estudaintes 
        except:
            print("Ingrese solo numeros validos")
            
    estudiantes[matricula] = {
         'nombre': nombre,
         'asignaturas': asignaturas
     }

def Consultar_estudiante():
    if not estudiantes:
        print("No hay datos")
        return
    
    for idMatricula, datos in estudiantes.items():
        print(f"ID del estudiante", idMatricula)
        print(f"Nombre: {datos['nombre']}")
        
        print("Asignatura")
        
        for asignatura, notas in datos['asignaturas'].items():
            print(f"- {asignatura}. {notas}")
        
def Calcular_promedio():
    if not estudiantes:
        print("No hay datos")
        return
    
    matricula = input("Ingrese la matricula del estudiante para ver su promedio: ")
    
    if matricula not in estudiantes:
        print("Estudiante no encontrado")
        return
    datos = estudiantes[matricula]
    print(f"Matricula: {matricula}")
    print(f"Nombre: {datos['nombre']}")
    
    print("Promedio por asignaturas ")
    for asignatura, notas in datos['asignaturas'].items():
        if notas:
            promedio = sum(notas) / len(notas)
            print(f" {asignatura}: {promedio:.2f}")
        else:
            print(f"= {asignatura}: Sin notas registradas")
def Eliminar_estudiante():
    pass

def Salir():
    print("Saliendo..")

while True:
    Menu()
    opc = input("Ingrese una opcion: ")

    match opc:
        case "1":
            Agregar_estudiante()
        case "2":
            Consultar_estudiante()
        case "3":
            Calcular_promedio()
        case "4":
            Eliminar_estudiante()
        case "5":
            Salir()
            break
        case _:
            print("Ingrese una opcion correcta ")
