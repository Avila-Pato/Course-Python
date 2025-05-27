n = int(input("Ingresa N: "))
a, b = 0, 1
secuencia = [a, b]

while b <= n:
    siguiente = a + b
    if siguiente > n:
        break
    secuencia.append(siguiente)
    a, b = b, siguiente

print(secuencia)