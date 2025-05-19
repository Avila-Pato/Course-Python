
asistentes = []


pregunta = str(input("desea agrear un usuario ? (si/no): \n")).lower()


while pregunta == "si":

        agregar = str(input("Ingrese el nombre del usuario; \n")).strip()
        asistentes.append(agregar)
        print(asistentes)
    
        pregunta = str(input("desea agregar otro? (si/no) \n"))
        
    
if pregunta == "no":
    print("cerrando..")
else:
    print("Respuesta no válida. Por favor escriba 'si' o 'no'.")

#Strip() elimina espacio
#lower() covierte las entradas en minusculas

