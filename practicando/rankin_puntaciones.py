puntuaciones = [450, 800, 1200, 300]

user = int(input("Ingrese su punuacion "))

puntuaciones.append(user)
puntuaciones.sort(reverse=True) ## Orden descendente de (mayor a menor) puede ser por defecto simplemente sacandole (reverse=True

print(puntuaciones)
