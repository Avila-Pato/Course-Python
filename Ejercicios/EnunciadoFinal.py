import os

if os.system("cls") !=0: os.system("clear")

productos = {
            '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'], 
            '2175HD':  ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], 
            'JjfFHD':  ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], 
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'], 
            'GF75HD':  ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'], 
            '123FHD':  ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], 
            '342FHD':  ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], 
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
            }

stock = {
            '8475HD': [387990,10], 
            '2175HD': [327990,4],
            'JjfFHD': [424990,1], 
            'fgdxFHD': [664990,21],
            '123FHD': [290890,32],
            '342FHD': [444990,7], 
            'GF75HD': [749990,2],
            'UWU131HD': [349990,1],
            'FS1230HD': [249990,0], 
} 
# //cambios

def menu():
    print(" *** MENU PRINCIPAL *** ")
    print("1. Stock marca. ")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. salir")
    
def stock_marca():
    stock_total = 0
    
    marca = input("Ingrese marca a consultar: ").strip()
    encontrado = False 
    for idx, datos in productos.items():
        nombre_marca = datos[0]
        if nombre_marca.lower() == marca.lower():
            if idx in stock:
                cantidad = stock[idx][1]
                stock_total += cantidad
                encontrado= True
    
    if encontrado:
        print(f"El stock es: {stock_total}" )
        
    if not encontrado:
        print("El producto no se encuentra")
            

def búsqueda_precio():
    try:
        p_min = int(input("Ingrese el precio Minimo: "))
        p_max = int(input("Ingrese el precio Maximo: "))
    except:
        print("Debe ingresar valores Enteros")
        return
    encontrado = False
    for idx, dato in stock.items():
        dinero = dato[0]
        if p_min < dinero and p_max > dinero:
            if idx in productos:
                marca = productos[idx][0]
                print(f"Los noteBooks entre los precios consultas son:  {marca}  | ID {idx}")
                encontrado = True
    if not encontrado:
        print("No se encuentra Productos con esos precios")

def actualizar_precio():

    # UWU131HD
    while True:
        modelo = input("Ingrese el modelo a actualizar: ") 

        encontrado = False
        for idx, dato in productos.items():
            if modelo == idx:
                if idx in stock:
                    try:
                        precio_nuevo =  int(input("Ingrese el precio nuevo: "))
                    except:
                        print("Ingrese un valor numerico ")
                    stock[idx][0] = precio_nuevo  
                    print(f"Precio actualizado a {precio_nuevo}" )
                encontrado = True
                modelo = input("Desea actualizar otro precio (s/n)?: ")
                if modelo == "n":
                    print("Regresando al menu")
                    return
                else:
                    break                    
        if not encontrado:
            print("El modelo no existe ")
    
def Salir():
    print("Programa finalizado ")
    
while True:
    menu()
    opc = input("Ingrese una opcion: ")
    
    match opc:
        case "1":
            stock_marca()
        case "2":
            búsqueda_precio()
        case "3":
            actualizar_precio()
        case "4":
            Salir()
            break
        case _:
            print("Ingrese una opcion valida") 