from os import system 

if system("clear") != 0: system("cls")

contador = 0 

while contador <= 10:
    print(contador)
    contador += 1 # contador = contador + 1 es improtante para no entrar en un bucle infinito

# utilziando la palarba break para salir del bucle
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

# continue, hace saltar la iteracion actual y continua con la siguiente

print("\n Bucle con continue")
contador = 0 
while contador <= 10:
    contador += 1
    if contador == 5:
        continue
    print(contador)

print("\n Bucle conw hile else")
contador = 0 
while contador <= 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")
