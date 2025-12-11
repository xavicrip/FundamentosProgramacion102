# ============================================
# Uso de variables globales y locales
# ============================================

#Variable global
contador = 0

def incrementar_local(x):
    x += 1  # Variable local
    print(x)

def incrementar_global():
    global contador
    contador += 1
    print(contador)

#invocar a las funciones
valor = 5
incrementar_local(valor)

incrementar_global()
incrementar_global()
incrementar_global()

# Ejemplo que integre uso completo de funciones

# Variable Globar - arreglo
registro_estudiantes = []

def agregar_estudiante(nombre, notas=None):
    if notas is None:
        notas = []
    registro_estudiantes.append((nombre, notas))

def agregar_nota(nombre, nota):
    for i, (n, notas) in enumerate(registro_estudiantes):
        if n == nombre:
            notas.append(nota)
            registro_estudiantes[i] = (n, notas)
            return
    print(f"Estudiante {nombre} no encontrado.")

def calcular_promedio(notas):
    if not notas:
        return None
    return sum(notas) / len(notas)

def reporte(nombre=None, minimo_aprobado=10):
    if nombre is None:
        # reporte general (no retorna nada)
        print("Reporte general de estudiantes:")
        for n, notas in registro_estudiantes:
            prom = calcular_promedio(notas)
            estado = "Aprobado" if (prom is not None and prom >= minimo_aprobado) else "Reprobado/No evaluado"
            print(f" - {n}: notas={notas} promedio={prom} -> {estado}")
        return

    # Si se pide un estudiante específico, retornamos datos
    for n, notas in registro_estudiantes:
        if n == nombre:
            prom = calcular_promedio(notas)
            return {"nombre": n, "notas": notas, "promedio": prom, "aprobado": (prom is not None and prom >= minimo_aprobado)}
    return None

# --- Uso del programa ---
# 1) Añadir estudiantes (funciones que no retornan)
agregar_estudiante("Carla", [12, 15, 14])
agregar_estudiante("Diego")   # sin notas al crear

# 2) Agregar notas (mutación)
agregar_nota("Diego", 9)
agregar_nota("Diego", 11)
agregar_nota("NoExiste", 10)  # demostración de manejo simple

# 3) Calcular promedios (función que retorna)
prom_carla = calcular_promedio([12, 15, 14])
print("Promedio Carla:", prom_carla)

# 4) Reporte general (función sin retorno) y reporte individual (con retorno)
reporte()  # imprime todos
info_diego = reporte(nombre="Diego", minimo_aprobado=10)  # paso por nombre
print("Info Diego (retornada):", info_diego)

# 5) Mostrar estado de la variable global
print("Registro global final:", registro_estudiantes)
