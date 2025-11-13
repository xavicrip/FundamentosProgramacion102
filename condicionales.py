# ============================================
# Estructuras condicionales - Simples, dobles, multiples
# ============================================
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
print()

# 1. Numeros positivo
num = -12
if num > 0:
    print(f"El {num} es positivo")
else:
    print(f"El {num} es negativo")
print()

#2. Numeros pares
num_par = 12345678998653
if num_par % 2 == 0:
    print(f"El numero {num_par} es par")
else:
    print(f"El numero {num_par} es impar")
print()

# 3. Sueldo empleado
sueldo = 17786

if sueldo > 0 and sueldo <= 475:
    print(f"El sueldo {sueldo} es basico")
elif sueldo > 475 and sueldo <= 1000:
    print(f"El sueldo {sueldo} es SP1")
elif sueldo > 1000 and sueldo <= 5000:
    print(f"El sueldo {sueldo} es SP2")
elif sueldo > 5000 and sueldo <= 10000:
    print(f"El sueldo {sueldo} es SP3")
else:
    print(f"El sueldo {sueldo} es de un alto ejecutivo")

# 4. Condicional multiple para validar texto
cargo = "asistente"

if cargo == "gerente":
    bono = 370
elif cargo == "subgerente":
    bono = 200
elif cargo == "operador":
    bono = 150
else:
    bono = 0
print(f"Cargo {cargo}: -> Bono = {bono}")
print()
