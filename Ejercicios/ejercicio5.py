# En una gran Multi-Tienda nacional se están realizando descuentos por el fin de temporada. Los descuentos vigentes son los siguientes: 

# Jeans      10% 
# Chaqueta   20% 
# Zapatos    15% 

# Estos descuentos se aplican por unidad y sólo a los productos vigentes.  

# Desarrolle un programa en PSeInt que permita determinar el total de una venta en la MultiTienda considerando un producto.  El programa debe solicitar por pantalla el tipo (Jeans, Chaqueta ó Zapatos), la cantidad y precio del producto. Se debe validar que la cantidad y precio sean valores mayores a 0.  

import os

if os.system("clear") !=0: os.system("cls")
Descuento_Jeans = 0
CantidadJeans = 0
PrecioJeans= 15000
total= 0
try:
    
    CantidadJeans = int(input("Ingrese la cantidad de jeans \n")) 

    if CantidadJeans >= 1:
        Descuento_Jeans = (CantidadJeans * PrecioJeans) * 0.10
        total = f"{PrecioJeans - Descuento_Jeans:.0f}"
    else:
        print("Ingrese un valor valido")

    if CantidadJeans >= 1:    
        print(f"total  descuento pr la cantidad de {CantidadJeans} Jeans es de ${Descuento_Jeans} en total serian ${total}")
    
except ValueError:
    print("no valido")
    
  

