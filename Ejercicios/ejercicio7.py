# En su lugar de trabajo existe una máquina donde puede adquirir bebidas. Existen tres opciones de bebida: coca-cola, fanta y sprite. El valor de cualquiera de ellas es: $400. 

# Desarrolle un programa que permita vender una bebida y entregar vuelto si así se determina.   

# El programa debe solicitar por pantalla el tipo de bebida que va a comprar: 1) coca-cola, 2) fanta o 3) sprite (validar opción). Además, se debe pedir el dinero a pagar por la bebida. 

# Si el dinero es igual a $400 no tiene vuelto. 
# Si el dinero es mayor a $400 debe entregar vuelto. 
# Si el dinero es menor a $400 debe mandar un mensaje de alerta. 

# Una vez que la venta finaliza debe mostrar el dibujo de la bebida adquirida, el cual será entregado por el docente.  
import os

if os.system("clear") !=0: os.system("cls")



# cantidadFanta = 0
# cantidadCoca = 0
# cantidadSprite = 0

precios = 400
dinero = int(input("Ingrese su dinero "))

print(("Ingrese la bebida que desea"))
bebidas = int(input("1.Coca-Cola\n2.Fata\n3.Sprite\n"))


if dinero == precios:
    print("Gracias por su compra")
elif dinero > precios:
    print(f"Gracias por su compra su vuelto es {dinero - precios}")
else:
    print("No hay suficiente dinero")




 
# if bebidas == 1:
#     cantidadCoca += 1
#     CocaColatotal = (cantidadCoca * coca_cola)
#     sobrante = (dinero - coca_cola)
#     print(f"Gracias por su compra su vuelto es {sobrante}")
# elif bebidas == 2:
#     cantidadFanta += 1
#     FantaTotal = (cantidadFanta * fanta)
#     sobrante = (dinero - fanta)
   
# elif bebidas == 3:
#     cantidadSprite += 1
#     SpriteTotal = (cantidadSprite * sprite)
#     sobrante = (dinero - coca_cola)
#     print(f"Gracias por su compra su vuelto es {sobrante}")
# else:
#     print("Ingrese una bebida dentro de als categorias")

