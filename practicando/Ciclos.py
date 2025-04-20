import os

# Precios por tipo de bulto
precioLiviano = 1000
precioGrande = 2000

# Limpieza de pantalla
if os.system("clear") != 0:
    os.system("cls")

# Entrada
NumBultos = int(input("\nIngrese la cantidad de bultos: "))

# Inicializamos los contadores
contadorLiviano = 0
contadorGrande = 0

# Bucle para ingresar los pesos de cada bulto
for i in range(NumBultos):
    pesoBulto = float(input(f"\nIngrese el peso del bulto #{i + 1} (1kg a 10kg): "))

    if 1 <= pesoBulto <= 5:
        contadorLiviano += 1
    elif 6 <= pesoBulto <= 10:
        contadorGrande += 1
    else:
        print("⚠️ Peso no válido. Debe estar entre 1kg y 10kg.")

# Resultados
totalLiviano = contadorLiviano * precioLiviano
totalGrande = contadorGrande * precioGrande

print(f"\nHay {contadorLiviano} bultos livianos. Total a pagar: ${totalLiviano}")
print(f"Hay {contadorGrande} bultos grandes. Total a pagar: ${totalGrande}")
