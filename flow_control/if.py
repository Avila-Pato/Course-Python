# # Sencentias condicionales (if, elif, else)


from os import system
if system("clear") != 0: system("cls")

edad = 18 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# ademas de usar if y else, se puede usar elif para determinar 
# multiples condiciones, teniendo en cienta que se ejecutara solo el primer bloque 
# si la condicion lo cumple


nota = str() 

if nota >= 9:
    print("Sobresaliente")
elif (nota >= 7) and (nota < 9):
    print("Notable")
elif (nota >= 5) and (nota < 7):
    print("Aprobado")
else:
    print("Suspendido")

#Los operadore slogicos en python son
# and: true si ambas condiciones son verdaderas
# or: true si al menos una de las condiciones es verdadera
# not: true si la condicion es falsa

#En javascript se usan los operadores
# &&: true si ambas condiciones son verdaderas
# ||: true si al menos una de las condiciones es verdadera
# !: true si la condicion es falsa
tiene_carnet = True

if edad >= 18 or tiene_carnet:
    print("Puedes entrar")
else:
    print("No puedes ingresar") 

#Tambien tenemos al operador "not"
#Negando una condicion

sesion_iniciada = False

if not sesion_iniciada:
    print("Inicia sesion")

#se pueden anidar condicionales dentro de otro condicional

edad =20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes entrar")
    else:
        print("No tienes dinero")
else:
    print("No eres mayor de edad")

# Más fácil sería:
# if edad < 18:
#   print("No puedes entrar a la disco")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa") 

# En pyhon son evaluadas como verdadero o falsos
# Los valores verdaderos son: True, 1, "hola", [1,2,3], (1,2,3)
print = 5

numero = 1

if numero: 
    print("El numero es verdadero")

numero = 0
if numero:
    print("El numero es falso")

# Los valores falsos son: False, 0, "", [], (), None

##Tambien podemos crear los ternarios
edad = 18
mensaje =  "Eres amyor de edad" if edad >=18 else "ES MENOR DE EDAD"
print(mensaje)

# Ejercicios

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("Determine el mayor de dos numeros")

num1 = input("Ingrese 1 numero:\n")
num2 = input("Ingrese 2 numero:\n")

if num1 > num2: 
     print("El numero", num1 ,"es mayor al" ,num2)
elif num2 > num1:
    print("El numero", num2 ,"es mayor al" ,num1)
else:
    print("El valor es invalido")


mensaje = f"El numero {num1} es mayor al {num2}" if num1 > num2 else f"El numero {num2} es mayor al {num1}"
print(mensaje)
    
        
# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("Calculadora")

num1 = int(input("Ingrese 1 numero:\n"))
num2 = int(input("Ingrese 2 numero:\n"))

operacion = input("Que operacion desea  (+, -, *, /) ") 

suma = (num1 + num2)
resta = (num1 - num2)
dividir = (num1 / num2)
multiplicar = (num1 * num2)

if operacion == "+":
    print(suma)
elif operacion == "-":
    print(resta)
elif operacion == "/":
    print(dividir)
elif operacion == "*":
    print(multiplicar)
else:
    print("Operacion invalida")




# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)