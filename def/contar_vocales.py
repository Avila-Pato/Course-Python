def contar_vocales(vocal):
    vocales = 0
    for c in vocal:
        if c in "aeiouAEIOU":
                vocales = vocales + 1
    return vocales
    

print(contar_vocales("Python es genial"))  # 5
