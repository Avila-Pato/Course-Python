#Ejemplo tipo de diccionario 

persona = {
    "nombre": "Diego",
    "apellido": "Garcia",
    "edad": 23,
    "es_estudianete": True,
    "calificaciones": [7, 8, 9, 10],
    "socials": {
        "facebook": "diego.garcia",
        "instagram": "diego.garcia",
        "twitter": "diego.garcia"
    }
}
#Acceder a los valores
print(persona)
print(persona["es_estudianete"])
print(persona["calificaciones"][2])
print(persona["socials"]["facebook"])
# Modificar valores
persona["es_estudianete"] = False
persona["edad"] = 24
print(persona)

# Agregar valores
persona["direccion"] = "Calle 123"
print(persona)

#Eliminar valroe o completamente al estudiante
del persona["es_estudianete"]
print(persona)

#Sobrescribir un diccionario con otro diccionario
print("-------------")
a = { "name": "John", "age": 30 }
b = { "city": "New York", "age": 40 }
c = { **a, **b }
print(c)

print("-------------")
#Comprobra si existe una propiedad
print("name" in persona) #False
print("-------------")
print("name" in persona.keys()) #false
print("-------------")
#Obtener todas las claves
print(persona.keys())
print("-------------")
#Obtener todos los valores
print(persona.values())
print("-------------")
#Obtener tanto clave como valor
print(persona.items())