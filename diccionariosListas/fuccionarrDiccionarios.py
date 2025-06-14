# Ejemplo:
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
# Salida esperada:
# {'a': 1, 'b': 3, 'c': 4}

#Uso el método items y list para crearme una lista

list1 = list(dic1.items())
list2 = list(dic2.items())

combine = dict(list1 + list2)
print(combine)

# Creamos una copia para no modificar dic1
resultado = dic1.copy()
resultado.update(dic2)

print(resultado)