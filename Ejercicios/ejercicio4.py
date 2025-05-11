# Se realizó una fiesta de bienvenida a todos los alumnos de inicio del Duoc. En esta fiesta, se cobraron los siguientes valores para las entradas: 

# Alumnos de inicio Duoc entrada liberada. 
# Alumnos antiguos Duoc $1.500. 
# Alumnos de otras instituciones $2.500. 

 

# Desarrolle un algoritmo y un programa en pseudocódigo que permita determinar el total de las ganancias de la fiesta.  Escribir el resultado considerando que asistieron a la fiesta: 

# x alumnos de inicio Duoc. 
# y alumnos antiguos Duoc. 
# z alumnos de otras instituciones. 



yAlumnos= 1500
zAlumnos= 2500


x = int(input("Ingresela cantidad de alaumnos de inicio \n"))
y = int(input("Ingresela cantidad de alaumnos antiguos  \n"))
z = int(input("Ingresela cantidad de alaumnos  otras isntitucioes\n"))

Totaly = ( y * yAlumnos)
TotalZ =(z * zAlumnos)

ganancias = Totaly + TotalZ

print(f"Alumnosde de inicio nopapgan, alumnosantiguos pagan unvalorde {Totaly} Alumnos de otras instituciones {TotalZ}")
print(f"Las ganancias son {ganancias}")