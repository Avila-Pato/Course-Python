###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###
import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

text = "Porque pytho, es P@rque, P0rque nose, P$rque "
pattern = "P.rque"

matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)

if(matches):
    print("El patrón se encuentra en la cadena de texto.")
else:
    print("El patrón no se encuentra en la cadena de texto.")

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la" # Hola, H0la, H$la  
##La r significa que el string es un raw string y no se interpretan los metacaracteres

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


# Cómo usar la barra invertida para anular el significado especial de un símbolo

text = "Mi casa es blanca. Y el coche es negro.."

pattern = r"\."

matches = re.findall(pattern, text)
print(matches)

# \d: coincide con cualquier dígito (0-9)

text = "El número de teléfono es 123456789"
found = re.findall(r'\d{2}', text)

print(found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi teléfono es +34 123456789"
found = re.findall(r'\+34 \d{2}', text)

print(found)

# Ejercicio: Detectar si hay un número de chileno en el texto gracias al prefijo +56

text = "Mi teléfono es +56 123456789"
found = re.findall(r'\+56 \d{2}', text)

print(found)