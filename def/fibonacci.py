
#   formula finonacci
# F(n)= F(n−1)+F(n−2)
def fibonacci_hasta(n):
    if n < 0:
         print("Ingrese un numero mayor a 0")
         exit()
    
    if n > 1:
        return fibonacci_hasta(n - 1) + fibonacci_hasta(n - 2)
    return n

for i  in range(10):
   resultado = fibonacci_hasta(i)
   if resultado is not None:
    print(i, resultado)
