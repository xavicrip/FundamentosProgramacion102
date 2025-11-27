# Llenar una matriz 3 x 3
matriz = []

print(" Ingresar los valores de la matriz 3 x 3 ")

for fila in range(3):
    fila_actual = []
    for columna in range(3):
        valor = int(input(f"Ingrese el valor {fila} - {columna}: "))
        fila_actual.append(valor)
    matriz.append(fila_actual)
print(matriz)
# imprimir por fila
for fila in matriz:
    print(fila)
