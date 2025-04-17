from os import system
if system("clear") != 0: system("cls")

print("Ejemplo de booleanos")

print("5 > 3: ", 5 > 3) # True
print("5 < 3: ", 5 < 3) # False
print("5 == 5:", 5 == 5) # Igual (True)
print("5 != 3:", 5 != 3) # Diferente (True)
print("5 >= 3:", 5 >= 3) # Mayor o igual (True)
print("5 <= 3:", 5 <= 3) # Menor o igual (False)

print("\nComparaciones con cadenas")    
print("'Hola' == 'Hola':", 'Hola' == 'Hola') # True
print("'Hola' != 'Hola':", 'Hola' != 'Hola') # False
print("'Hola' == 'hola':", 'Hola' == 'hola') # False
print("'Hola' != 'hola':", 'Hola' != 'hola') # True
print("'pera' > 'manzana':", 'pera' > 'manzana') # False
## Es true porque 'pera' es lexicográficamente mayor que 'manzana' en el alfabeto ASCII 
# (p > m) p tiene un vadlor de 112 y m de 109
print("'pera' < 'manzana':", 'pera' < 'manzana') # True



# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)             # False
print("not False:", not False)            # True

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)


