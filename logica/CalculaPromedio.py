# Desarrolle un programa en Python que permita calcular el promedio final de la asignatura de programación de algoritmos de un estudiante. El programa debe permitir ingresar la nota de la experiencia de aprendizaje 1, 2 y 3. Donde cada nota tiene una ponderación de 30%, 40% y 30%. Este promedio (promedio de presentación de examen) debe mostrarse por pantalla.  

# Luego, el programa debe permitir ingresar la nota del Examen transversal y calcular el promedio final. Recuerde que el promedio final se calcula como 60% el promedio de presentación y 40% la nota del examen. 

# Ambos promedios mostrados por pantalla deben ir redondeados con un número decimal. Siga el ejemplo a continuación: 

# Ejemplo 1: 

# Ingrese la nota de la EA1: 4 
# Ingrese la nota de la EA2: 5.2 
# Ingrese la nota de la EA3: 6.1 
# El promedio de presentación final es: 5.1 
# Ingrese la nota del examen: 4.0 
# El promedio final es: 4.7 

import os

if os.system("clear") !=0: os.system("cls")

not1 = input("Ingrese la nota de la EA1 \n")
not2 = input("Ingrese la nota de la EA2 \n")
not3 = input("Ingrese la nota de la EA3 \n")
examen = input("Ingrese su nota de examen \n")

promedio = (float(not1)* 0.3 + float(not2) * 0.4 + float(not3) * 0.3)
promedioExamen = (float(promedio) * 0.6 + float(examen) * 0.4)

resultado = f"{promedioExamen:.1f}"

print(f"Su promedio de notas es {promedio}")
print(f"Su promedio final es {resultado}")