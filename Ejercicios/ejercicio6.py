# En un Gimnasio se está realizando una encuesta para determinar la edad promedio de las personas que asisten a él. Existen tres categorías: 

# Entre 10 y 17 años             niño 
# Entre 18 y 29 años             joven 
# Entre 30 y 50 años            adulto 

# Las personas que asisten al gimnasio deben estar entre estos rangos de edad. 
# Desarrolle un programa que permita determinar: 
# El promedio de edad de las personas que asisten al gimnasio 
# La cantidad de mujeres y hombres que asisten al gimnasio 
# La cantidad final por categoría 
# El programa debe solicitar por pantalla el sexo (F ó M) y la edad de la persona (validar datos de entrada). 
import os

if os.system("clear") !=0: os.system("cls")
adulto = 0
joven = 0
niño = 0 
cantidad= 0
Masculino = 0
Femenino = 0
personas = 0

try:
    cantidad = int(input("Inrese la cantidad de persnas \n"))
except ValueError:
 print("Ingrese un numero valido")

for i in range(cantidad):
    personas +=  1

    sexo = str(input(f"Ingrese el genero de la {personas} persona (f\m) \n")).lower()
    if sexo not in ["f", "m"]:
        print("Ingrese un gener valido valida ")
        break

    if sexo == "f":
        Masculino += 1
    elif sexo == "m":
        Femenino += 1 


    edad = int(input("Ingrese su edad \n"))
    if edad > 0 and edad < 10:
        niño += 1
    elif edad > 11 and edad < 29:
        joven += 1
    elif edad > 30 and edad < 50:
        adulto +=  1
    else:
        print("Ingrese un valor valido")

   
if cantidad > 0:
    print(f"total de niño es {niño} ")
    print(f"total de jovene es {joven} ")
    print(f"total de aadulto es {adulto} ")
    print(f"Total mujeres {Masculino}")
    print(f"Total Hmbres {Femenino}")


