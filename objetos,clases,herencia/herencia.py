class Animal:
    def __init__(self, nombre, onapoteya):
        self.nombre = nombre
        self.onapoteya = onapoteya
    def saludo(self):
        print("Hola, soy un ", self.tipo, "y mi sonido es el", self.onapoteya )
        
class Gato(Animal):
    tipo = 'gato'
class Perro(Animal):
    tipo= 'perro'
    
gato = Gato("Flufly", "Maullido")
gato.saludo()

perro = Perro("Firulais ", "ladrido")
perro.saludo()        
