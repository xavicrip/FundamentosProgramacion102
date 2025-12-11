# ============================================
# FUNCIONES
# ============================================

# Funcion que devuelve valor

def sumar(a,b):
    resultado = a+b
    return resultado

print(sumar(2,3))
print(sumar(300,900))
print(sumar(-2,9))
print(sumar(30,-900))

# funcion para calcular el promedio
def promedio(numeros):
    promedio = sum(numeros)/len(numeros)
    return promedio

print(promedio([4,6,8,20,80,88,6]))

# Funiones que no devuelven valor

def saludar(nombre):
    print("Hola", nombre)

saludar("Wayner")
saludar("Byron")
saludar("Estefany")
saludar("Xavier")

# Funcion para agregar elementos a una lista

def agregar_elemento(lista, elemento):
    lista.append(elemento)

mi_lista = [1,2,3]
agregar_elemento(mi_lista, 4)
agregar_elemento(mi_lista, 7)
agregar_elemento(mi_lista, 9)
agregar_elemento(mi_lista, 27)
print(mi_lista)
