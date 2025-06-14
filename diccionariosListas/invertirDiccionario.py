# Ejemplo:
dic = {'a': 1, 'b': 2, 'c': 3}
# Salida esperada:

# {1: 'a', 2: 'b', 3: 'c'}
reserve = {clave: valor for valor, clave in dic.items()}

print(reserve)