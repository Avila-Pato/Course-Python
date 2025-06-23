def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial:", factorial(5))  # Resultado: 120


def factorial(n):
    result = 1
    for i in  range(1,n+1):
        result *= i
    return result
print("Factorial:", factorial(5))