# and, or, not


# How can i use and operator

edad = 18

edad = int(input("Escriba su edad: "))

vip = str(input("tiene entrada al vip? si/no").strip().lower())


if edad >= 18 and vip == "si":
    print("Puedes entrar")
else:
    print("No puedes ingresar") 

# how can i use or operator 

edad = int(input(" Ingrese su edad: "))
tiene_tarjeta = str(input("Tiene tarjeta? ").strip().lower())

if edad >= 18 or tiene_tarjeta:
    print("Felicidades tienes un descuento")
else: 
    print(" Lo siento no tienes descuento")

# How can i use not

sesion_iniciada = input(" Esta inicaida la sesion: ")

if not sesion_iniciada:
    print("Debes inicair sesion para continuar")
else :
    print(" Bienvenido al sistema")

# How can use use all the operators


tiene_boleto = input("Tienes boleto ? ").strip().lower()
edad = int(input("Ingrese su edad: "))
lista_negra = input("Estas en la lsita negra ? ").strip().lower()

if (tiene_boleto or edad < 18 ) and not lista_negra:
    print("Puedes viajar en tren ")
else:
    print("No puedes Viajar en tren")
