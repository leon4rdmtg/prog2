NUM_FILAS = 5
NUM_COLUMNAS = 7
#  Crea la sala como matriz de asientos, cada uno con estado y precio
def crear_sala(filas, columnas):
    return [[{"estado": "L", "precio": 50} for _ in range(columnas)] for _ in range(filas)]

#  Muestra el estado visual de la sala con encabezado de columnas
def mostrar_sala(sala):
    print("\n🎬 Estado actual de la sala:")
    print("      ", end="")
    for c in range(1, len(sala[0]) + 1):
        print(f"{c:2}", end=" ")
    print()
    for i, fila in enumerate(sala):
        print(f"Fila {i + 1:<2} -> ", end="")
        for asiento in fila:
            simbolo = "O" if asiento["estado"] == "O" else "L"
            print(f"{simbolo:2}", end=" ")
        print()
    print("L = Libre, O = Ocupado")

#  Ocupa un asiento individual e informa su precio (cambio nuevo)
def ocupar_asiento(sala, fila, columna):
    try:
        asiento = sala[fila][columna]
        if asiento["estado"] == "O":
            print("❌ Ese asiento ya está ocupado.")
            return False
        else:
            asiento["estado"] = "O"
            precio = asiento["precio"]
            print(f"✅ Asiento en Fila {fila + 1}, Columna {columna + 1} reservado.")
            print(f"💰 Precio: Bs {precio}")  # NUEVO: muestra el precio
            return True
    except IndexError:
        print("❌ Asiento inválido. Verifique fila y columna.")
        return False

#  Cuenta asientos libres en toda la sala
def contar_asientos_libres(sala):
    return sum(asiento["estado"] == "L" for fila in sala for asiento in fila)

#  Busca asientos contiguos (grupo en la misma fila)
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

#  Reserva asientos contiguos y muestra el total (cambio nuevo)
def ocupar_asientos_juntos(sala, fila, inicio_columna, cantidad):
    total = 0
    for j in range(inicio_columna, inicio_columna + cantidad):
        sala[fila][j]["estado"] = "O"
        total += sala[fila][j]["precio"]
    print(f"🎟️ {cantidad} asientos reservados en fila {fila + 1}, columnas {inicio_columna + 1} a {inicio_columna + cantidad}.")
    print(f"💰 Total a pagar: Bs {total}")  # NUEVO: suma de precios

#  BUSQUEDA ALTERNATIVA: Agrupa bloques de asientos libres en varias filas
def buscar_agrupaciones(sala, cantidad):
    agrupaciones = []  # Lista de tuplas (fila, inicio_columna, cantidad_en_bloque)
    for i, fila in enumerate(sala):
        j = 0
        while j < len(fila):
            if fila[j]["estado"] == "L":
                inicio = j
                largo = 0
                while j < len(fila) and fila[j]["estado"] == "L":
                    largo += 1
                    j += 1
                agrupaciones.append((i, inicio, largo))
                if sum(gr[2] for gr in agrupaciones) >= cantidad:
                    return agrupaciones
            else:
                j += 1
    return []

#  FUNCION NUEVA: Ocupa asientos de varias filas si no hay contiguos
def ocupar_agrupaciones(sala, agrupaciones, cantidad):
    asientos_reservados = 0
    total = 0
    for fila, inicio, largo in agrupaciones:
        for j in range(inicio, inicio + largo):
            if sala[fila][j]["estado"] == "L":
                sala[fila][j]["estado"] = "O"
                total += sala[fila][j]["precio"]
                print(f"✅ Asiento reservado en fila {fila + 1}, columna {j + 1}")
                asientos_reservados += 1
                if asientos_reservados == cantidad:
                    print(f"💰 Total a pagar: Bs {total}")  # NUEVO: total para reserva separada
                    return
    print("⚠️ No se pudo reservar la cantidad solicitada.")

#  Bucle principal del programa
sala = crear_sala(NUM_FILAS, NUM_COLUMNAS)
while True:
    print("\n🎟️ MENÚ DE OPCIONES")
    print("1. Ver sala")
    print("2. Reservar un asiento")
    print("3. Reservar varios asientos juntos o separados")
    print("4. Contar asientos libres")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_sala(sala)

    elif opcion == "2":
        try:
            fila = int(input(f"Ingrese número de fila (1-{NUM_FILAS}): ")) - 1
            columna = int(input(f"Ingrese número de columna (1-{NUM_COLUMNAS}): ")) - 1
            ocupar_asiento(sala, fila, columna)
        except ValueError:
            print("⚠️ Entrada no válida. Debe ingresar números.")

    elif opcion == "3":
        try:
            cantidad = int(input("¿Cuántos asientos quiere reservar?: "))
            if cantidad > NUM_COLUMNAS * NUM_FILAS:
                print("❌ No hay tantos asientos disponibles en la sala.")
                continue

            # PRIMER INTENTO: Buscar asientos juntos
            fila, inicio = buscar_asientos_juntos(sala, cantidad)
            if fila is not None:
                ocupar_asientos_juntos(sala, fila, inicio, cantidad)
            else:
                print(" No hay suficientes asientos contiguos disponibles.")

                # SEGUNDO INTENTO: Buscar agrupaciones en varias filas (nuevo comportamiento)
                sugerencias = buscar_agrupaciones(sala, cantidad)
                if sugerencias:
                    print(" Sugerencias de asientos disponibles:")
                    total_mostrado = 0
                    for grupo in sugerencias:
                        fila_id, inicio_col, largo = grupo
                        print(f" - {largo} libres en fila {fila_id + 1}, columnas {inicio_col + 1} a {inicio_col + largo}")
                        total_mostrado += largo
                        if total_mostrado >= cantidad:
                            break

                    confirmar = input("¿Desea reservarlos aunque estén separados? (s/n): ").lower()
                    if confirmar == "s":
                        ocupar_agrupaciones(sala, sugerencias, cantidad)  # NUEVO: activa reserva separada
                    else:
                        print(" Reserva cancelada.")
                else:
                    print("😕 No hay suficientes asientos libres aunque estén separados.")
        except ValueError:
            print("⚠️ Entrada no válida. Debe ingresar un número.")

    elif opcion == "4":
        libres = contar_asientos_libres(sala)
        print(f"📊 Asientos disponibles: {libres}")

    elif opcion == "5":
        print("👋 Gracias por usar el sistema de reservas.")
        break
    else:
        print("⚠️ Opción inválida. Intente nuevamente.")