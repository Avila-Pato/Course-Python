
lista = ['banana', 'banana', 'manzana', 'pera', 'pera', 'frutilla' ]

nueva_listta = set(lista)
print(nueva_listta)




productos = ["manzana", "pera", "manzana", "plátano", "pera", "naranja", "plátano"]
productos_no_reptidos = []

for producto in productos:
    if productos not in productos_no_reptidos:
        productos_no_reptidos.append(producto)
    print(productos_no_reptidos)