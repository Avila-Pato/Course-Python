total = 0

while True:
    entrada = input("Ingresa un número o 'stop': ")
    
    try:
        entrada_str = str(entrada)
        if entrada_str == "stop":
            break
        
        entrada_int = int(entrada)
        total += entrada_int
    except ValueError:
        print("Entrada inválida")

print(f"Suma total: {total}")