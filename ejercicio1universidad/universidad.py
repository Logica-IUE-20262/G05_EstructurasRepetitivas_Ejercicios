# Programa: Ingreso a la universidad
# Ejercicio 1B - Comparación con operadores lógicos (AND y OR combinados)
#
# Reglas de ingreso en la IUE:
# - El carnet solo sirve si la persona sigue estudiando (si no estudia,
#   el carnet queda desactivado) -> se necesitan AMBAS cosas (AND).
# - Un egresado recibe un carnet especial (carnet de egresado) que
#   por si solo permite el ingreso (OR).
# - Tener la aplicación Ulises activa también permite el ingreso por
#   si sola (OR).

tiene_carnet = input("¿Tiene carnet vigente? (si/no): ").strip().lower()
esta_estudiando = input("¿Actualmente está estudiando en la IUE? (si/no): ").strip().lower()
es_egresado = input("¿Es egresado con carnet de egresado? (si/no): ").strip().lower()
tiene_ulises = input("¿Tiene la aplicación Ulises activa? (si/no): ").strip().lower()

if (tiene_carnet == "si" and esta_estudiando == "si") or es_egresado == "si" or tiene_ulises == "si":
    print("Puede ingresar a la universidad.")
else:
    print("No puede ingresar a la universidad.")