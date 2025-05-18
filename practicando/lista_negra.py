lista_negra = ["ana", "luis", "pedro"]


visitante = str(input("Inrese su nombre \n"))


if visitante in lista_negra:
    print("No puede ingresar")
elif visitante not in lista_negra:
    print("bienvenido")
else:
    ("inrese un numero valido")