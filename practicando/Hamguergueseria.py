## Hambuergueseria : 2HojasLechuga + 2RodajasTomates = 1PorcionPalta

## Una lechuga tiene 20 hojas
# 1 tomate tiene 5 rodajas (3 tomates  )
# 1 una palta tiene 5 porciones (2 paltas )


# Con los valores ingresados, cuantas hambuerguesas genero? 
# en caso que no alcance para una hambuerguesa, cuantos ingredientes pfaltan para una hambuerguesa

import os

if os.system("clear") !=0: os.system("cls");

## cantidad de ingredientes totales en bodegga
lechuga = 20
tomate = 15
palta = 10

##cantidad porciones para 1 hamburguesa
cantHojas = 2
cantTomate= 2
cantPalta = 1
print("Ingredientes para crear la Hamburguesa")

print(" 1 PorcionPalta")
print(" 2 HojasLechuga")
print(" 2 RodajasTomates ")




print("")

print("------------------Bodega----------------")
print("hojas de Lechuga", lechuga)
print("rodajas de tomate", tomate) 
print("porciones palta", palta)  
print("------------------Bodega----------------")


## total que se tiene en mano
faltanteTomate = (tomate - cantTomate) % 2

print("------------Total porciones en mano------------")
totalCanLehuga = int(lechuga / cantHojas )
print("lechuga en hojas ", totalCanLehuga)

totalCantTomate = int(tomate / cantTomate)

print(f"tomates en rodajas {totalCantTomate}")

totalCantPaltas = int(palta / cantPalta)
print("paltas porciones",totalCantPaltas)

# hamburguesas que puedo hacer

hamburguesas = min(totalCanLehuga,  totalCantTomate, totalCantPaltas)

if hamburguesas > 0:
    print(f"puedo hacer {hamburguesas} hamburguesas, si desea agregar otra le falta {faltanteTomate} de rodaaj de tomate")
else:
    print("Bueno adios")











