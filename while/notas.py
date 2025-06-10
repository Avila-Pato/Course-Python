##Ingresar 3 listas con 5 notas cada 1 y sacar el promedio de cada estudiante y e promedio del curso

# Listas de notas
lista1 = [4.0, 5.0, 4.0, 2.0, 6.0]
lista2 = [6.0, 5.0, 4.0, 4.0, 7.0]
lista3 = [2.0, 2.0, 4.0, 2.0, 5.0]


lista = {
    "Lista 1": lista1,
    "Lista 2": lista2,
    "Lista 3": lista3,
}

# .items() es muy útil cuando se nececita  acceder tanto a la clave como al valor dentro de un diccionario

# La clave es "Lista 1", "Lista 2", "Lista 3".
# El valor es la lista de notas correspondiente.

# Recorrer cada lista
for listaName, notas in lista.items():
    # Copiar la lista original para no modificar el original directamente
    notas_filtradas = notas.copy()
    # Eliminar la peor nota (mínimo)
    notas_filtradas.remove(min(notas_filtradas))
    # Eliminar la mejor nota (máximo)
    notas_filtradas.remove(max(notas_filtradas))
    print(f"{listaName} Actualizacion: {notas_filtradas}")



estudiante1 = float(sum(lista1) / len(lista1))
estudiante2 = float(sum(lista2) / len(lista2))
estudiante3 = float(sum(lista3) / len(lista3))


print("Promedio del estudiante 1:", estudiante1)
print("Promedio del estudiante 2:", estudiante2)
print("Promedio del estudiante 3:", estudiante3)



promedio_curso = (estudiante1 + estudiante2 + estudiante3) / 3
print(f"\nPromedio del curso: {promedio_curso:.1f}")


