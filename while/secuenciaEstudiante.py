# Construir un programa que registre las notas de una cantidad determinada de estudiantes,
# validando que cada nota esté entre 1.0 y 7.0. Si el usuario se equivoca al ingresar una nota (por ejemplo, pone texto o un número fuera de rango), 
# el programa debe volver a pedir esa misma nota.

# Pedir al usuario cuántos estudiantes hay en total.
# Usa un bucle while para validar que el número sea entero positivo.
# Crear un bucle for para iterar la cantidad de estudiantes.
# Para cada estudiante, muestra: "Estudiante 1", "Estudiante 2", etc.
# Dentro del for, usar un while para pedir la nota del estudiante.


# Si el valor ingresado no es un número (try-except) o está fuera del rango 1.0 a 7.0, 
# mostrar un mensaje de error y volver a pedir la nota del mismo estudiante.
# No avanzar al siguiente estudiante hasta que se ingrese una nota válida.

# Ir acumulando todas las notas para calcular el promedio al final.
# Al terminar, mostrar el promedio general de notas de los estudiantes.

# 🧪 Validaciones que debes aplicar:
# El número de estudiantes debe ser entero positivo.
# Cada nota debe ser:
# numérica (try-except)

# mayor o igual a 1.0
# menor o igual a 7.0

import os

if os.system("clear") != 0:
    os.system("cls")
notas_estudiantes = []
estudiantes = 0



while estudiantes <=0:
    try:
        estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
        if estudiantes < 0:
            print("numero positivos porfavor")
    except Exception:
        print("ingrese un valor valido")



for i in range(estudiantes):
    estudiantes_valido = False

    while not estudiantes_valido:
        try:
            nota = float(input(f"Ingrese las nota del estudiante {i + 1}"))
            if 1.0 <= nota <= 7.0:
                estudiantes_valido =True
                notas_estudiantes.append(nota)
            else:
                print("Ingrese un valor enre el rango 1.0 a 7.0,")
        except Exception :
            print("Ingrese un numer valido")


for indice in notas_estudiantes:
    print(f"Estudiante", notas_estudiantes.index(indice) + 1, ":", indice)
        
        
promedio = sum(notas_estudiantes) / len(notas_estudiantes)
print(f"\n📊 Promedio general: {promedio:.2f}")
