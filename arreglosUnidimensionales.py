# ============================================
# Arreglos Unidimensionales
# ============================================

# Declarar el arreglo
# Ingresar 5 nombres en el arreglo

nombres = []

# 1. Ingresar datos en el arreglo
# Ingresa 5 veces los nombres
for i in range(5):
    nombres.append(input(f"Ingrese nombre, en las posicion: {i}: "))

# 2. Imprimir o mostrar los datos ingresados en el arreglo
print()
print("Lista de nombres: ")
for nombre in nombres:
    print(nombre)

