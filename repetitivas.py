# ============================================
# Estructuras repetitivas - while
# ============================================

#contador = 1
#while True:
#    print(f"El resultado es: {contador}")
#    contador += 2
#    if contador >= 99:
#        break
#print("El resultado es: ", contador)


# Ejemplo 2: Suma de numeros

#suma = 0
#num = 5
#while num != 0:
#    suma += num
#    print(f"El resultado es: {suma}")
#    num = int(input("Ingrese un numero:" ))
#print(f"El resultado FINAL ES: {suma}")


# Ejemplo 3: Ciclos repetitivos con String

password = "1234567"
pass_validar = input("Ingrese la contaseña: ")

if pass_validar == password:
    print("Bienvenido al sistema")
else:

    i = 1
    while i<3 and pass_validar != password:
        print("El password es incorrecto")
        pass_validar = input("Ingrese nueva clave: ")
        i = i + 1
if(i==3):
    print("NO INGRESO AL SISTEMA, CUENTA BLOQUEADA")
    print(f"El nuevo password es: {pass_validar} y  realizo {i} intentos fallidos" )
else:
    print(f"Bienvenido al sistema, Ud. uso {i-1} intentos fallidos")
