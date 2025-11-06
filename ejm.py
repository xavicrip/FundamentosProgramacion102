# Unidad 2: Fundamentos de Progracion
#2.2 Manejo de variables y tipos de datos

nombre = "Xavier"
edad = 42
nota = 8.5
activo = True

# Ejemplos para mostrar el valor y su tipo:
print(nombre, type(nombre))
print(edad, type(edad))
print(nota, type(nota))
print(activo, type(activo))

# Ejercicios practicos con tema 2.2

# 1. Vamos a declara variables de un estudiante

#Ingreso de datos a las variables

mi_nombre = "Byron"
mi_edad = 41
mi_estatura = 170.4
soy_estudiante = False


print("Ingrese Nombre", mi_nombre);
print("Ingrese Edad", mi_edad);
print("Ingrese Estatura", mi_estatura);
print("Es estudiante", soy_estudiante);
print()

# 2. Crear 2 variables base y altura mostra por mensaje
base = 20
altura = 5
print(f"base: {base}, altura: {altura}")
print()

# 3. Pedir ingresar valores por teclado
# usa input

#nombre_usuario = input("Ingrese Nombre de usuario: ")
#password = input("Ingrese Password: ")
#correo = input("Ingrese Correo: ")

# imprimirlos
#print(nombre_usuario, correo)
#print(f"Nombre de usuario: {nombre_usuario} y Correo: {correo}")
print()

# Trabajar con operaciones matematicas
numUno = 15
numDos = 8.7

print(numUno, type(numUno))
print(numDos, type(numDos))

# Operaciones aritmeticas: + - * / % // **
print("Suma = ", numUno + numDos)
print("Resta = ", numUno - numDos)
print("Multiplicacion = ", numUno * numDos)
print("Division = ", numUno / numDos)
print("Division Entera= ", numUno // numDos)
print("Residuo = ", numUno % numDos)
print("Potencia= ", numUno ** numDos)

m = ((numDos + numUno) / 2) * (5 + (numUno%numDos))
print("El resultado es: ", m)

# Operadores Relaciones
print("numUno es mayor a numDos", numUno > numDos)
print("numDos es menor a numUno", numDos < numUno )
print("numDos es menor a numUno", numDos == numUno )

print("numDos es menor a numUno o diferente a numUno = ", numDos > numUno or numDos == numUno )

# Ejemplo para calcular el area del triangulo
baseTriangulo = 6
alturaTriangulo = 5
areaTriangulo = (baseTriangulo * alturaTriangulo)/2
print("El resultado es: ", areaTriangulo)

# precio de un producto mas el iva
precioProducto = 20
ivaPorcentaje= 15
calculoIva = precioProducto * (ivaPorcentaje / 100)
precioFinal = precioProducto + calculoIva
print("El resultado es: ", precioFinal)










