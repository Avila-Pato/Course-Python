
import os
import random
if os.system("clear") !=0: os.system("cls")
num1 = 0
num2 = 0
num1 = int(input("Ingrese el limite inferior "))
num2 = int(input("Ingrese el limte superior "))
print("Tienes un maximo de 3 intentos adivina el numero")
ramdonNumero = random.randint(num1,num2)
intenos = 0
maxIntentos = 3
adivina = 0
while maxIntentos > intenos:
 
    intenos += 1
 
adivina = int(input("Intente adivinar: "))
 
if adivina == ramdonNumero:
 
        print(f"Lo lograste el numero random es {ramdonNumero} en el intento {intentos}")
        exit()
elif adivina > ramdonNumero:
 print("el numero es menor ")
elif adivina < ramdonNumero:
 print("el numero es mayor ")
 print(f"Te dare una pista el numeroe sta mas cerca del {ramdonNumero + 1} que del 2 ")
else:
 print("Ingrese una opcion valida")
if intenos == 3:
 print(f"Lo siento se te acabaron los turnos el numero era {ramdonNumero}")