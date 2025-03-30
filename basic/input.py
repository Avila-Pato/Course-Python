
###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###


from os import system
if system("clear") != 0: system("cls")


# Para obtener datos del usuario se usa la función input()
# La función input() recibe un mensaje que se muestra al usuario
# y devuelve el valor introducido por el usuario

nombre = input("Ingrese su nombre\n")
print(f"Hola  {nombre} Encantado")

# la funcion input() devuelve un valor de tipo string
# si queremos obtener un nuemero se debe convertir el string a numero
age = input("Cuantos a;os tienes>\n")
age = int(age)

print(f"tu edad es {age}")

#La funcion input() Permite tambien devolver multiples valores 
# separados por comas

print("Obteniedno multiples valores")

country, city = input("En que pais y ciudad vives\n").split(" ")
print(f"Tu pais es {country} y tu ciudad es {city}")
