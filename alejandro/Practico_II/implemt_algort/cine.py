def crear_sala(filas, columnas):
    return [[{"estado": "L", "precio": 50} for _ in range(columnas)] for _ in range(filas)]
def mostrar_sala(sala):
    print("\n🎬 Estado actual de la sala:")
    for i, fila in enumerate(sala):
        print("Fila", i + 1, end=" -> ")
        for asiento in fila:
            simbolo = "O" if asiento["estado"] == "O" else "L"
            print(simbolo, end=" ")
        print()
    print("L = Libre, O = Ocupado")

def ocupar_asiento(sala, fila, columna):
    try:
        asiento = sala[fila][columna]
        if asiento["estado"] == "O":
            print(" Ese asiento ya está ocupado.")
            return False
        else:
            asiento["estado"] = "O"
            print(f" Asiento en Fila {fila + 1}, Columna {columna + 1} reservado.")
            return True
    except IndexError:
        print(" Asiento inválido.")
        return False
def contar_asientos_libres(sala):
    return sum(asiento["estado"] == "L" for fila in sala for asiento in fila)
def buscar_asientos_juntos(sala, cantidad):
    for i, fila in enumerate(sala):
        consecutivos = 0
        inicio = 0
        for j, asiento in enumerate(fila):
            if asiento["estado"] == "L":
                if consecutivos == 0:
                    inicio = j
                consecutivos += 1
                if consecutivos == cantidad:
                    return i, inicio
            else:
                consecutivos = 0
    return None, None
def ocupar_asientos_juntos(sala, fila, inicio_columna, cantidad):
    for j in range(inicio_columna, inicio_columna + cantidad):
        sala[fila][j]["estado"] = "O"
    print(f"🎟️ {cantidad} asientos reservados en fila {fila + 1}, columnas {inicio_columna + 1} a {inicio_columna + cantidad}.")
# Ejecución del sistema de cine
filas = 5
columnas = 7
sala = crear_sala(filas, columnas)
while True:
    print("\n🎟️ MENÚ DE OPCIONES")
    print("1. Ver sala")
    print("2. Reservar un asiento")
    print("3. Reservar varios asientos juntos")
    print("4. Contar asientos libres")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        mostrar_sala(sala)
    elif opcion == "2":
        fila = int(input("Ingrese número de fila (1-5): ")) - 1
        columna = int(input("Ingrese número de columna (1-7): ")) - 1
        ocupar_asiento(sala, fila, columna)
    elif opcion == "3":
        cantidad = int(input("¿Cuántos asientos quiere reservar juntos?: "))
        fila, inicio = buscar_asientos_juntos(sala, cantidad)
        if fila is not None:
            ocupar_asientos_juntos(sala, fila, inicio, cantidad)
        else:
            print("❌ No hay suficientes asientos contiguos disponibles.")
    elif opcion == "4":
        libres = contar_asientos_libres(sala)
        print(f"📊 Asientos disponibles: {libres}")
    elif opcion == "5":
        print("👋 Gracias por usar el sistema de reservas.")
        break
    else:
        print("⚠️ Opción inválida. Intente nuevamente.")
print(" fin del programa ----- jose alejandro zabala romero")