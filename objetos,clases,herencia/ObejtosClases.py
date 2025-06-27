class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

usuario_1 = Usuario("Pato", "Avila")
usuario_2 = Usuario("Isaias", "Andres")

print(usuario_1.nombre, usuario_1.apellido)
print(usuario_2.nombre, usuario_2.apellido)    
        