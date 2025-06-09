

num = int(input("Ingrese un numero"))


pares = 0
impares = 0

for i in range(1,  num):
    if i % 2 == 0:
        print(f" {i} es par")
        pares +=1
    elif i % 2 == 1:
        impares += 1
        print(f"{i} Es impar")

if pares > 0 and impares > 0:
    print(f"Pares totales {pares} ")
    print(f"imparees totales {impares}")