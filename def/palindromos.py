def es_palindromo(texto):
   
    return texto == texto[::-1]  


print(es_palindromo("oso"))        # True
print(es_palindromo("reconocer"))  # True
print(es_palindromo("python"))     # False
