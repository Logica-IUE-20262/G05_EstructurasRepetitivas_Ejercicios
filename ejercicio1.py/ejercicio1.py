# Programa: Ingreso a la discoteca
# Ejercicio 1A - Comparacion con operadores logicos (AND)
#
# Para poder ingresar, el visitante debe cumplir AMBAS condiciones
# al mismo tiempo: ser mayor de edad Y tener cédula.

edad = int(input("Ingrese su edad: "))
tiene_cedula = input("¿Tiene cedula? (si/no): ").strip().lower()

if edad >= 18 and tiene_cedula == "si":
    print("Puede ingresar a la discoteca.")
else:
    print("No puede ingresar a la discoteca.")