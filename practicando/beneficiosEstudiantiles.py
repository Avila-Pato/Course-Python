




carrera = str(input("Ingrese su carrera: \n")).lower()
try: 
    actividad_fisica = int(input("Ingrese als horas a la semana practicando actividad fisica : \n"))
except Exception :
    print("Ingrese un numero valido")
    exit()

# end try


lista = ["kinesiología", "educación física", "nutrición"]

if carrera in lista:
    if actividad_fisica > 5:
        print("Puede entreaar con acceso  grattuito al  gimnacio")
    elif actividad_fisica < 3: 
        print("Tienesun descuento del 50%")        
    else:
        print("Su carrera no se encuentra no recibe  beneficio")

if carrera not in lista:
    print("Su carrera no se encuentra en los datos")

