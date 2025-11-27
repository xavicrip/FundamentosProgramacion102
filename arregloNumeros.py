# ============================================
# Arreglos Unidimensionales
# ============================================

numeros = [10,9,8,7,5,7,8,4,8,9,9,7,10,10,8,9,9]

#calcular el promedio
suma = 0
for n in numeros:
    suma += n

promedio = suma / len(numeros)

print("El promedio es: ", promedio)