
##Encuentra el número faltante
números = [1, 2, 3, ..., 45, 46, 48, ..., 100]  # falta el 47



números = list(range(1, 47))  + list(range(48, 101)) ##Aqui genere 2 listas range(1, 47) y range(48, 100) 
##y luego las concatene y las sume obteniedo una lista del a1 al 100 excluyendo el 47
print(números)


suma_teorica = (100 * 101) // 2 ##Suma teorica Suma de 1 a n = n × (n + 1) ÷ 2 + 100 * 101 // 2 = 5050


print(suma_teorica)

## suma_actual = 5050 - 47 = 5003
suma_actual = sum(números) # Esto calcula la suma real de la lista actual 
print(suma_actual)


faltante = suma_teorica - suma_actual

print(f"Falta el número: {faltante}")  
