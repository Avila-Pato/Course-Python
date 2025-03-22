# Ejemplo de uso de if, elif y else

edad = 20

if edad < 18:
    print("Eres menor de edad.")
elif edad < 65:
    print("Eres un adulto.")
else:
    print("Eres una persona mayor.")

# Ternarios
mensaje = "Eres mayor de dad" if edad > 17 else "eres menor de edad"  
print(mensaje)
