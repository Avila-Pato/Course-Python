import os

if os.system("clear") != 0: os.system("cls")

print("Calculadora")

print("1_sumar\n2_restar\n3_multiplicar\n4_dividir")

resultado = input("Ingrese la operacion deseada\n ")
num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))

if resultado == "1" or resultado == "sumar":
    print(num1 + num2)
elif resultado == "2" or resultado == "restar":
    print(num1 - num2)
elif resultado == "3" or resultado == "multiplicar":
    print(num1 * num2)
elif resultado == "4" or resultado == "dividir":
    print(num1 / num2)
    
