datos = {'nombre': 'Ana', 'edad': 25, 'ciudad': None}

limpio = {clave: valor for valor, clave in datos.items() if valor is not None}
print(limpio)