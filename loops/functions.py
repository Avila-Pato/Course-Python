def suma(a, b):
    suma = a + b
    return suma
resultado = suma(1,2)
print(resultado)


def describir_persona(nombre: str, apellido: str, edad: int):

    print(f"{nombre} {apellido} tiene {edad} años")

describir_persona("Patricio", "Avila", 18)
print(describir_persona("Patricio", "Avila", 18))