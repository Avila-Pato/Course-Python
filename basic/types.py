"""
El comando type() permite comprobar el tipo de objeto en Python

"""

print("int:" ) #entero numero sin aprte decima/
print(type(10)) # Numero entero Positivo
print(type(0)) # Numero entero 
print(type(-10)) # Numero entero Negativo
print(type(12342345234235235)) # Python permite almacenar numeros enteros de gran tama;o


print("float:") # Numero con parte decimal con punto flontante
print(type(10.5)) # Numero con parte decimal con punto flontante
print(type(1.0)) # otro ejemplo float
print(type(1e3)) #Notacion cientifica equivale a 1*10^3 = 1000

print("complex:") # Numero complejo (como parte real e imaginaria)
print(type(1+2j)) # Numero complejo con parte real e imaginaria

print("str:") # Cadena de texto
print(type("HOLA")) # Cadena de texto
print(type('HOLA')) # Cadena de texto
print(type("""HOLA""")) # Cadena de texto

print("bool:") # Booleano
print(type(True)) # Booleano
print(type(False)) # Booleano
print(type(1< 2)) # Booleano

print("NoneType:") # representa la asucencia de valor
print(type(None)) #None es un  tipo especial que representa sin valor o nulo