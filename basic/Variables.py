

# Las variables sirven para guardar datos en memoria.

from os import system
if system("clear") != 0: system("cls")

#Para asignar una varialb e solo hace falta poner el nombre de la variavle y asignarle un valor

my_name = "Pato"
print(my_name)

age = 32
print(age)

#Podemos reasignar un nuevo valor a una variable existente
age = 39
print(age)

#Tipado dinamico:  el tipo de determina en tiempo de ejecuciom
# no es necesario declariar expliciamente el tipo de la variable

name = "pato"
print(type(name))

name = 3
print(type(name))

#Tipado fuerte: Pyrthon no realiza conversiones de tipo automatico
# print(10 + "10") # ❌ Esto genera un error de tipo

#La conversion correcta seria
print(10 + int("10"))

#Forma recomendata de declarar f-string
print(f"hola soy {my_name}, tengo {age - 13} años")

#Conversiones de nombre de variables correctament
mi_nombre_de_variable = "okay" #snake_case
mi_nombre_de_variable_123 = "ok"

#Conversiones de nombre de variables incorrectas

miNombreDeVariable = "no-recomendado" # camelCase
MiNombreDeVariable = "no-recomendado" # PascalCase
minombredevariable = "no-recomendado" # todojunto


# para declarar constantes usamos mayusculas
MI_CONSTANTE = 3.14


is_user_logged_in: bool = True # Indica que la variable es un booleano
print(is_user_logged_in)

name: str = "pato" # Indica que la variable es una cadena de texto
print(name)
