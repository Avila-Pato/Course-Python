c = open('../leyendoArchivos/texto.txt', "a") ##Append

c.write("\n Hola soy un texto nuevo agregado")
c.close()

x = open('../leyendoArchivos/texto.txt', "w") ##write
print(x.read())

# Elimianr archivos usando una libreria

import os 

# os.remove("texto.txt")

if os.path.exists("texto.txt"):
    os.remove("texto.txt")
else:
    print("El archivo no existe")

