# Realizar un pseudocódigo, diagrama de flujo y código que permita estar en un menú hasta que el
# usuario decida salir. Identifique las instrucciones, tipos de datos y los contadores o
# acumuladores usados

print("EL MENU DEL RESTAURANTE INFINITO PARA EL DIA DE HOY ES")
print("seleccionar alguna de las opciones para la solicitud de la comida")
print("1. bandeja paisa : 32.500")
print("2. ajiaco : 27.050")
print("3. arroz con camarones: 35.750")
print("4. sancocho: 30.525")
print("5. salir del menú")

opciones_menu = int(input("Ingrese su opción: "))

cantidad_bandeja = 0
cantidad_ajiaco = 0
cantidad_camarones = 0
cantidad_sancocho = 0
total_platos = 0
saldo_cuenta = 0

while opciones_menu != 5:
    if opciones_menu == 1:
        print("Agregada con exito")
        saldo_cuenta += 32500
        cantidad_bandeja += 1
        total_platos += 1
    elif opciones_menu == 2:
        print("Agregada con exito")
        saldo_cuenta += 27050
        cantidad_ajiaco += 1
        total_platos += 1
    elif opciones_menu == 3:
        print("Agregada con exito")
        saldo_cuenta += 35750
        cantidad_camarones += 1
        total_platos += 1
    elif opciones_menu == 4:
        print("Agregada con exito")
        saldo_cuenta += 30525
        cantidad_sancocho += 1
        total_platos += 1
    else:
        print("Opción no válida.")

    print("\n¿Desea agregar algo más?")
    print("1. bandeja paisa : 32.500")
    print("2. ajiaco : 27.050")
    print("3. arroz con camarones: 35.750")
    print("4. sancocho: 30.525")
    print("5. salir del menú")
    opciones_menu = int(input("Ingrese su opción: "))

print("Haz salido con exito")
print(f"La cantidad de platos solicitados es de: {total_platos}")
print("De los cuales estan repartidos en: ")
print(f"Bandejas paisa: {cantidad_bandeja}")
print(f"ajiacos: {cantidad_ajiaco}")
print(f"arroz con camarones: {cantidad_camarones}")
print(f"sancocho: {cantidad_sancocho}")
print(f"La cuenta es de: {saldo_cuenta} Muchas gracias por visitarnos")