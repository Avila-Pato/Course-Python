#  Limpiar la consola:

# Usar os.system("clear") si es Unix o os.system("cls") si es Windows.
# Detectar cuál usar probando si uno falla.

# Inicializar el bucle principal del menú:
# Utiliza while True para mostrar el menú repetidamente hasta que el usuario elija salir.
# Mostrar el menú de opciones dentro del bucle:

# Opción 1: Tarjeta de crédito
# Opción 2: Carrito de compras
# Opción 3: Salir
# Solicitar al usuario una opción con input.
# Verificar la opción ingresada con if, elif, else:

# Si elige "1":
# Mostrar deuda de $100,000.
# Pedir al usuario un depósito.
# Validar que sea número.
# Evaluar si es menor, igual o mayor que la deuda.
# Mostrar el resultado correspondiente (saldo restante, deuda saldada, vuelto).

# Si elige "2":
# Inicializar saldo_tarjeta = 100000 y total = 0.
# Crear un bucle while para registrar compras.
# Dentro del bucle:
# Preguntar monto o si desea salir.
# Si escribe "salir", salir del bucle.
# Validar que el monto sea número positivo.
# Verificar si hay saldo suficiente.
# Descontar el saldo, sumar al total y mostrar resultado.
# Al final del bucle, mostrar total gastado y saldo restante.

# Si elige "3":
# Imprimir mensaje de salida y terminar el programa con exit().
# Si no elige ninguna opción válida:
# Mostrar mensaje de error.
# Asegurarse de capturar errores con try/except:
# Para entradas no numéricas o errores imprevistos.
import os

if os.system("clear") !=0: os.system("cls")

print("Elija 1 opcion")

saldo_tarjeta = 100000
total= 0

while True:
    try:
        print("\n===== MENÚ =====")
        opc = int(input("\n1. Tarjeta  de credito\n2. Carrito de compras \n3. Salir\n"))
        if opc > 0:
            if opc == 1:
                firstBandera= True
                while firstBandera:
                    try:
                        print(f"Su deuda en la tarjeta es de {saldo_tarjeta:,.0f}".replace(",", "."))
                        sub_opc = int(input("\nIngrese su deposito\n"))
                    except ValueError:
                        print("Ingrese una opcion valida")
                    
                    if sub_opc < 0:
                        print("Ingrese un monto valido")
                    elif sub_opc < saldo_tarjeta:
                        saldo_restante = sub_opc - saldo_tarjeta
                       
                        print(f"Gracias por su abono  su saldo restante es {abs(saldo_restante):,.0f}".replace(",","."))
                      
                    elif sub_opc == saldo_tarjeta:
                        print("has saldado tu saldo_tarjeta")
                      
                    else:
                        vuelto = sub_opc // saldo_tarjeta
                        print(f"Deuda saldada. tu saldo  restante es {abs(vuelto):,.0f}".replace(",","."))
                    firstBandera = False
                    
            elif opc == 2:
                
                while True:
                    monto = input("Si desea salir ingrese (salir) \n  Ingrese su compra\n")
                    
                    if monto == "salir":
                        print("Saliendo...")
                        break
                    
                    monto_int = int(monto)
                    
                    if monto_int < saldo_tarjeta:
                        total = monto_int + total
                        descuento_total = monto_int - saldo_tarjeta
                        print(f"gracais por su compra de {abs(total):,.0f}".replace(",","."))
                        print(f"su saldo restante es de {abs(descuento_total):,.0f}".replace(",",(".")))
                    elif monto_int > saldo_tarjeta:
                        print(f"sus fondos son insuficientes su saldo actual  es de {saldo_tarjeta}")

            elif opc == 3:
                print("Cerrando programa..")
                exit()

        
        else:
            print("ingrese una opcion correcta 1,2,3")
    except ValueError:
        print("Elija 1 opcion correcta")
 