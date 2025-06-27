class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def saludo(self):
        print("Hola, mi nombre es ", self.nombre, self.apellido)

usuario_1 = Usuario("Pato", "Avila")

usuario_1.saludo()  #Llama la funcion
usuario_1.nombre = "Maicol" #modifica el nombre
usuario_1.saludo()
del usuario_1.nombre #Borra el paramatro nombre
usuario_1.saludo()

        