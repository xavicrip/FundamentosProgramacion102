# ============================================
# Estructuras repetitivas - FOR
# ============================================

# Imprimir numeros de 1 - 100
for i in range(1, 5):
    print(i)
print()

# Letras de una cadena
mensaje = "Hola mundo"
for letra in mensaje:
    print(letra)
print()

# Imprimir numeros impares del 1 al 30
for i in range(2, 31, 2):
    print(i)
print()

# Imprimir la tabla de multiplicar
print("Tabla de multiplicar: ")
numero = int(input("Ingrese un numero: "))
while True:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break
print()


