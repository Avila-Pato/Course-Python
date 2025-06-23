
#   formula finonacci
# F(n)= F(n−1)+F(n−2)
# def fibonacci_hasta(n):
#     if n < 0:
#          print("Ingrese un numero mayor a 0")
#          exit()
    
#     if n > 1:
#         return fibonacci_hasta(n - 1) + fibonacci_hasta(n - 2)
#     return n




# for i  in range(10):
#    resultado = fibonacci_hasta(i)
#    if resultado is not None:
#     print(i, resultado)

def fibonaci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
print(fibonaci(10))


def fibonacci(n):
    a, b = 0,1
    for i in range(n):
        a, b =  b, a+ b
    return a
print(fibonacci(10))


        