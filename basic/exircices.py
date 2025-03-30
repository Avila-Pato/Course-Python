###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

# print("\nEjercicio 1: Imprimir mensajes")
# print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# nombre, ciudad = input("Escribe tu nombre y ciudad: ").split(" ")
# print(f"Mi nombre es {nombre} y mi ciudad es {ciudad}")

# nombre = input("nombre\n")
# print(f"tu nombre es {nombre}")

# ciudad = input("ciudad\n")
# print(f"Tu ciudad es {ciudad}")


### Completa aquí

print("--------------")

# print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
# print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
# a = 15
# b = 3.14159
# c = "Hola mundo"
# d = True
# e = None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))


### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

print(type(12345))
print(12345 + int("12345"))
print(12345 + float("12345"))







### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

nombre = "pato"
edad = 26
altura = 1.90



#Forma recomendata de declarar f-string

print(f"hola soy {name}, tengo {age - 13} años y mido {altura} cm")

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

# Solución:
    # Redondeamos directamente el valor de pi sin almacenarlo en una variable
resultado = int(round(3.1416) / 2)
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)