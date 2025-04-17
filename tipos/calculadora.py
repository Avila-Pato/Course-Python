import os
if os.system("clear") != 0: os.system("cls")

n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite outro número: '))
opc = str("Ingrese una opcion")

sum = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2



mensaje = f"""

para los numeros {n1} y {n2},

para los numenos de suma es {sum}
para los numenos de resta {resta}
para los numenos de multiplicación {multi}
para los numenos de división {div}
"""

print(mensaje)