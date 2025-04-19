import os
import time

if os.system("clear") != 0: os.system("cls")

contactos = []

class Contactos:
    def __init__(self, nombre, apellido, email, phone, birthday):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._phone = phone
        self._birthday = birthday

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday


def printMenu():
    print('\nSeleccione una opción:')
    print('[1] Crear contacto')
    print('[2] Listado de contactos')
    print('[3] Modificar contacto')
    print('[4] Eliminar contacto')
    print('[5] Buscar contacto')
    print('[6] SALIR')

def crear_contacto():
    print('\n--- Crear nuevo contacto ---')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    email = input('Email: ')
    phone = input('Teléfono: ')
    birthday = input('Cumpleaños (dd/mm/aaaa): ')

    nuevo_contacto = Contactos(nombre, apellido, email, phone, birthday)
    contactos.append(nuevo_contacto)
    print('✅ Contacto creado correctamente.')

def listar_contactos():
    print('\n--- Lista de contactos ---')
    if not contactos:
        print('No hay contactos guardados.')
    else:
        for idx, c in enumerate(contactos, start=1):
            print(f"[{idx}] {c}")
def actualizar_contacto():
    print('\n--- Modificar contacto ---')
    listar_contactos()
    if not contactos:
        print('No hay contactos para modificar.')
    else:
        try:
            idx = int(input('Ingrese el número del contacto que desea modificar: '))
            contacto = contactos[idx - 1]
            print('Ingrese los nuevos datos del contacto:')
            contacto.nombre = input('Nombre: ')
            contacto.apellido = input('Apellido: ')
            contacto.email = input('Email: ')
            contacto.phone = input('Teléfono: ')
            contacto.birthday = input('Cumpleaños (dd/mm/aaaa): ')
            print('✅ Contacto modificado correctamente.')
        except ValueError:
            print('Por favor, ingrese un número valido.')
        except IndexError:
            print('El contacto no existe.')

def buscar_contacto():
    print('\n--- Buscar contacto ---')
    listar_contactos()
    if not contactos:
        print('No hay contactos para buscar.')
    else:
        try:
            idx = int(input('Ingrese el número del contacto que desea buscar: '))
            contacto = contactos[idx - 1]
            print(contacto)
        except ValueError:
            print('Por favor, ingrese un número valido.')
        except IndexError:
            print('El contacto no existe.')

def borrar_contacto():
    print('\n--- Eliminar contacto ---')
    listar_contactos()
    if not contactos:
        print('No hay contactos para eliminar.')
    else:
        try:
            idx = int(input('Ingrese el número del contacto que desea eliminar: '))
            contactos.pop(idx - 1)
        #contactos.pop(idx - 1) basicamente es lo mismo que contactos.remove(contactos[idx - 1])
            print('✅ Contacto eliminado correctamente.')
        except ValueError:
            print('Por favor, ingrese un número valido.')
        #idx es el index del contacto que queremos borrar

def run():
    while True:
        printMenu()
        option = input('Opción: ')
        if option == '1':
            crear_contacto()
        elif option == '2':
            listar_contactos()
        elif option == '3':
            print('Modificar contacto (pendiente)')
        elif option == '4':
            borrar_contacto()
        elif option == '5':
            print('Buscar contacto (pendiente)')
        elif option == '6':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida')
            time.sleep(2)

def __str__(self):
        return f"{self.nombre} {self.apellido} | Email: {self.email} | Tel: {self.phone} | Cumpleaños: {self.birthday}"

if __name__ == "__main__":
    run()
