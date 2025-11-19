# ============================================
# Estructuras condicionales - Simples, dobles, multiples
# ============================================

# Ejemplo Menus
opcion = ""

while opcion != "4":
    print(f"------------MENU DE OPCIONES------------")
    print("1 - Suma")
    print("2 - Multiplicar")
    print("3 - Dividir")
    print("4 - Sair")
    opcion = input("Ingrese su opcion: ")
    if opcion == "1":
        suma = 4 + 7
        print(suma)
    elif opcion == "2":
        multiplicar = 7 * 4
        print(multiplicar)
    elif opcion == "3":
        dividir = 7 / 4
        print(dividir)
    elif opcion == "4":
        print("Saliendo")
        break