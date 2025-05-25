import os


os.system("cls" if os.name == "nt" else "clear")

totalIngresos = 0
cantidad_boletos = 0


while cantidad_boletos <= 0:
    try:
        cantidad_boletos = int(input("Ingrese la cantidad de boletos a vender: "))
        if cantidad_boletos <= 0:
            print("Ingrese un número positivo")
    except ValueError:
        print("Por favor, ingrese un número válido.")


for i in range(cantidad_boletos):

    precio_boleto = -1 # Valor inicial para que entre al while
    while precio_boleto < 0:
        try:
            precio_boleto = float(input(f"Ingrese el precio del boleto {i + 1}: "))
            if precio_boleto < 0:
                print("Ingrese un valor positivo.")
        except ValueError:
            print("Ingrese un valor numérico válido.")
            precio_boleto = -1  # Fuerza que se repita
    totalIngresos += precio_boleto

print(f"\nEl total de ingresos por la venta de boletos es: ${totalIngresos:.2f} dólares.")
