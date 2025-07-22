import random
FILAS = 4
COLUMNAS = 2
BARCOS = 3
# Crear un tablero vacío
def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
# Mostrar el tablero
def mostrar_tablero(tablero, ocultar_barcos=False):
    print("   " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        letra = chr(ord('A') + i)
        fila_mostrar = []
        for celda in fila:
            # Mejora visual: uso de símbolos más claros (~, B, X, *) en vez de números
            if celda == 0:
                fila_mostrar.append("~")  # Agua
            elif celda == 1:
                fila_mostrar.append("~" if ocultar_barcos else "B")  # Barco (oculto o visible)
            elif celda == 2:
                fila_mostrar.append("X")  # Tocado
            elif celda == 3:
                fila_mostrar.append("*")  # Fallo
        print(f"{letra}  " + " ".join(fila_mostrar))
    print()
# Conversión de coordenadas tipo "A1" a índices
def coord_a_indices(coord):
    # Validación agregada: evita errores si se ingresa mal la coordenada
    try:
        fila = ord(coord[0].upper()) - ord('A')
        columna = int(coord[1:]) - 1
        if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
            return fila, columna
    except:
        pass
    return None, None
# Colocar barcos aleatoriamente
def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            colocados += 1
# Ejecutar un disparo
def disparar(tablero_objetivo, tablero_disparos, coord, nombre):
    fila, columna = coord_a_indices(coord)
    if fila is None:
        print("Coordenada inválida. Intenta de nuevo.")
        return False  # Validación extra: coordenada fuera de rango o mal escrita
    if tablero_objetivo[fila][columna] == 1:
        tablero_objetivo[fila][columna] = 2
        tablero_disparos[fila][columna] = 2
        print(f"{nombre} hizo ¡Tocado!")
        return True
    elif tablero_objetivo[fila][columna] == 0:
        tablero_objetivo[fila][columna] = 3
        tablero_disparos[fila][columna] = 3
        print(f"{nombre} disparó al agua.")
        return True
    else:
        print("Ya se disparó allí.")  # Validación agregada para evitar repetir disparos
        return False
# Verificar si aún quedan barcos
def quedan_barcos(tablero):
    return any(1 in fila for fila in tablero)
# Guardar puntuación en archivo con marca de tiempo
def guardar_puntuacion(nombre):
    # Mejora: se incluye fecha y hora de la victoria
    from datetime import datetime
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre} ganó la partida - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
# Menú principal del juego
def juego():
    while True:
        print("=== Batalla Naval ===\n")
        # Reglas añadidas para mostrar al usuario antes de jugar
        print("📜 Reglas del juego:")
        print("- El objetivo es hundir todos los barcos del oponente.")
        print("- Cada jugador tiene un tablero de 4 filas (A–D) y 2 columnas (1–2).")
        print(f"- Se colocan automáticamente {BARCOS} barcos en posiciones aleatorias.")
        print("- En cada turno disparas a una coordenada (ej: A1).")
        print("- Si aciertas, se marca con 'X'. Si fallas, se marca con '*'.")
        print("- El primer jugador en destruir todos los barcos del rival gana.\n")

        print("1. Jugar contra la CPU")
        print("2. Jugar contra otro jugador")
        modo = input("Selecciona modo (1 o 2): ")
        if modo == "1":
            nombre_jugador = input("Tu nombre: ")
            nombre_cpu = "CPU"
            tablero_jugador = crear_tablero()
            tablero_cpu = crear_tablero()
            disparos_jugador = crear_tablero()
            disparos_cpu = crear_tablero()
            colocar_barcos(tablero_jugador, BARCOS)
            colocar_barcos(tablero_cpu, BARCOS)
            disparos_cpu_realizados = set()  # Se agrega para evitar disparos repetidos por la CPU
            turno = 1
            while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_cpu):
                print(f"\n--- Turno {turno} ---")
                print("Tu tablero:")
                mostrar_tablero(tablero_jugador)
                print("Tus disparos:")
                mostrar_tablero(disparos_jugador, ocultar_barcos=True)
                # Validación del disparo del jugador: solo avanza si es válido
                while True:
                    coord = input("Dispara (ej. A1): ")
                    if disparar(tablero_cpu, disparos_jugador, coord, nombre_jugador):
                        break
                if not quedan_barcos(tablero_cpu):
                    break
                # Lógica mejorada: la CPU no repite disparos
                while True:
                    fila_cpu = random.randint(0, FILAS - 1)
                    col_cpu = random.randint(0, COLUMNAS - 1)
                    if (fila_cpu, col_cpu) not in disparos_cpu_realizados and tablero_jugador[fila_cpu][col_cpu] in [0, 1]:
                        disparos_cpu_realizados.add((fila_cpu, col_cpu))
                        break
                coord_cpu = f"{chr(ord('A') + fila_cpu)}{col_cpu + 1}"
                print(f"{nombre_cpu} dispara a {coord_cpu}")
                disparar(tablero_jugador, disparos_cpu, coord_cpu, nombre_cpu)
                turno += 1
            if quedan_barcos(tablero_jugador):
                print(f"¡{nombre_jugador} gana!")
                guardar_puntuacion(nombre_jugador)
            else:
                print("¡La CPU gana!")
        elif modo == "2":
            nombre1 = input("Nombre del Jugador 1: ")
            nombre2 = input("Nombre del Jugador 2: ")
            tablero1 = crear_tablero()
            tablero2 = crear_tablero()
            disparos1 = crear_tablero()
            disparos2 = crear_tablero()
            colocar_barcos(tablero1, BARCOS)
            colocar_barcos(tablero2, BARCOS)
            turno = 1
            while quedan_barcos(tablero1) and quedan_barcos(tablero2):
                print(f"\n--- Turno {turno} ---")
                print(f"{nombre1}, este es tu turno")
                mostrar_tablero(disparos1, ocultar_barcos=True)
                while True:  # Validación: repetir si se dispara a una celda inválida
                    coord = input("Dispara (ej. A1): ")
                    if disparar(tablero2, disparos1, coord, nombre1):
                        break
                if not quedan_barcos(tablero2):
                    break
                print(f"\n{nombre2}, este es tu turno")
                mostrar_tablero(disparos2, ocultar_barcos=True)
                while True:  # Validación: repetir si se dispara a una celda inválida
                    coord = input("Dispara (ej. A1): ")
                    if disparar(tablero1, disparos2, coord, nombre2):
                        break
                turno += 1
            if quedan_barcos(tablero2):
                print(f"¡{nombre1} gana!")
                guardar_puntuacion(nombre1)
            else:
                print(f"¡{nombre2} gana!")
                guardar_puntuacion(nombre2)
        else:
            print("Opción inválida. Reinicia el programa.")
            return
        # Nueva opción: repetir juego si el jugador lo desea
        repetir = input("¿Deseas jugar otra vez? (s/n): ")
        if repetir.lower() != 's':
            break
juego()