"""
 Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente

"""
import re

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"

pattern = "IA"

found_ia = re.search(pattern, text)

if found_ia:
    print(f"El patrón se encuentra desde la posición {found_ia.start()} hasta la posición {found_ia.end()} en la cadena de texto.")
else:
    print("El patrón no se encuentra en la cadena de texto.")

### Encontrar todas las coincidencias de un patron
# .findall() devuelve una lista con todas las conicidencias


text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"

pattern = "Python"

matches = re.findall(pattern, text)

print(len(matches))

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"

pattern = "Python"

for match in re.finditer(pattern, text):
    print(match.group(), match.start(), match.end())

# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.

text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

pattern = "midudev"

matches = re.findall(pattern, text)
print(matches)

# re.IGNORECASE: Ignora las mayúsculas y minúsculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"

pattern = "ia"

matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)

# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.

text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"

pattern = "python"

matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)

### Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto

text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "adios"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)