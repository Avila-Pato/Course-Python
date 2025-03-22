
costoMadera = 5000 * 5000  
costoPiedra = 1000 * 2000 
costoPerfil = 4 * 200000   
costoClavos = 500 * 30    

totalCosto = costoMadera + costoPiedra + costoPerfil + costoClavos

print("El costo total de la construccion por casa es: $", {totalCosto})

ingresos = float(input("Ingrese sus ingresos totales: "))

CantidadC = int(input("Ingrese la cantidad de casas que desea comprar: "))


totalCostoCasas = totalCosto * CantidadC 

if ingresos >= totalCostoCasas:
    print("La cantidad es suficiente para construir ", {CantidadC}, "casas")
else: 
    print("No tienes suficiente dinero para construir ", {CantidadC}, "casas")

CasasPosibles = ingresos // totalCosto

# Convertir a entero
CasasPosibles = int(CasasPosibles)

print("Con su monto puede construir ", {CasasPosibles}, "casas")

DineroFaltante = totalCostoCasas - ingresos
DineroFaltante = int(DineroFaltante)

if CasasPosibles > 0:
    print("Necesita $", {DineroFaltante}, "para comprar ", {CasasPosibles}, "casas")
    