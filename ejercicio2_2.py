# Definición e ingreso de variables
numero_dado = int(input("Ingrese un numero entero: "))

# En tu código usas 'acumulador' como residuo inicial y luego como contador
acumulador = numero_dado % 2

if acumulador == 0:
    while acumulador <= numero_dado:
        print("Numero:", acumulador)
        acumulador = acumulador + 2
else:
    acumulador = 0
    while acumulador < numero_dado:
        print("Numero:", acumulador)
        acumulador = acumulador + 2