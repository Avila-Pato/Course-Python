"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

def count_carnivorous_eggs(egg_counts):
    total_carnivorous_eggs = 0

    for eggs in egg_counts:
        if eggs % 2 == 0:
            total_carnivorous_eggs += eggs

    return total_carnivorous_eggs

egg_counts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total_carnivorous_eggs = count_carnivorous_eggs(egg_counts)
print(total_carnivorous_eggs)
