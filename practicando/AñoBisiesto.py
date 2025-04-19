

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.


print("Año bisiesto")

año = int(input("Ingreseun año:\n"))

if ((año % 4 == 0)) and ((año % 100 != 0)) or (año % 400 == 0):
    print("El año es bisiesto")
else: 
    print("El año no es bisiesto")