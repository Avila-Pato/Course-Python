import os
if os.system("clear") != 0:
    os.system("cls")

arancel = 1800000
matricula = 90000
descuento_arancel = 0
descuento_matricula = 0 

promedio = float(input("Ingrese su promedio : "))
quintil = int(input("Ingrese el quintil entre (1 al 5): "))

# Descuento en el arancel
if promedio >= 6.0:
    if quintil in [1, 2]:
        descuento_arancel = 0.20
    elif quintil == 3:
        descuento_arancel = 0.15
    elif quintil == 4:
        descuento_arancel = 0.10
    elif quintil == 5:
        descuento_arancel = 0.0
elif 5.0 <= promedio < 6.0:
    if quintil in [1, 2]:
        descuento_arancel = 0.10
    elif quintil == 3:
        descuento_arancel = 0.05
    else:
        descuento_arancel = 0.0

# Descuento en la matrícula
if quintil in [1, 2, 3]:
    descuento_matricula += 0.10
if promedio >= 5.5:
    descuento_matricula += 0.05

# Cálculo de valores finales
monto_descuento_matricula = matricula * descuento_matricula
matricula_final = matricula - monto_descuento_matricula
monto_descuento_arancel = arancel * descuento_arancel
arancel_final = arancel - monto_descuento_arancel

# Resultados
print(f"Arancel final: ${arancel_final:,.0f}")
print(f"Matrícula final: ${matricula_final:,.0f}")
