class Animal:
    def __init__(self, nombre, onapoteya):
        self.nombre = nombre
        self.onapoteya = onapoteya
    def saludo(self):
        print("Hola, soy un ", self.tipo, "y mi sonido es el", self.onapoteya )
        
class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onapoteya):
        super().__init__(nombre, onapoteya)
        print("Instanciando el gato !!")
    
class Perro(Animal):
    tipo= 'perro'
    def __init__(self, nombre, onapoteya):
        super().__init__(nombre, onapoteya)
        print("Instanciando el perro!! ")
    
gato = Gato("Flufly", "Maullido")
gato.saludo()

perro = Perro("Firulais ", "ladrido")
perro.saludo()        
