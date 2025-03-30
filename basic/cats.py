# casting de types
# trasnformar un tipo de un valor a otro

from os import system
if system("clear") != 0: system("cls")

print("Conversion de tipos")

# Convertir una cadena que contiene un número a un entero y sumarlo con otro entero
print(2 + int("100")) #Convierte "100 " a entero y suma 2, resultado igual a 102

# Convertir una cadena con un número decimal a tipo float
print(float("2.5"))

# Convertir un número decimal a entero (se trunca la parte decimal)
print(int(3.23423)) # salida 3

# Evaluar valores numéricos como booleanos

print(bool(3)) # Cualquier numero distinto a 0 es true, resutlado true
print(bool(0)) # resultado false
print(bool("")) # resultado false
print(bool(" ")) # resultado true
print(bool(-43)) # resultado true

#redondear un numero decimal
print(round(2.51))

print(int("100"))

# print(int("hola mundo")) # error porque no es un numero
print(len("Hola mundo"))