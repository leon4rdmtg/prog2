import random
from datetime import datetime  # Para obtener la fecha y hora actual
# Constantes del tamaño del tablero y cantidad de barcos
FILAS = 4
COLUMNAS = 2
BARCOS = 3
# Crea un tablero vacío (matriz de ceros)
def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
# Coloca aleatoriamente los barcos (valor 1) en el tablero
def colocar_barcos(tablero):
    barcos_colocados = 0
    while barcos_colocados < BARCOS:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            barcos_colocados += 1
# Muestra el tablero con símbolos gráficos
def mostrar_tablero(tablero):
    print("  1 2")
    for i, fila in enumerate(tablero):
        linea = chr(65 + i) + " "  # Letras A-D como filas
        for celda in fila:
            if celda == 0:
                linea += "· "  # Agua no disparado
            elif celda == 1:
                linea += "■ "  # Barco propio (puede ocultarse si se desea)
            elif celda == 2:
                linea += "○ "  # Agua (fallo)
            elif celda == 3:
                linea += "X "  # Impacto (barco tocado)
        print(linea)
# Verifica si una coordenada ingresada es válida (ej. A1, B2, etc.)
def coord_valida(coord):
    if len(coord) != 2:
        return False
    fila = coord[0].upper()
    columna = coord[1]
    return fila in "ABCD" and columna in "12"
# Convierte una coordenada tipo A1 a índices de lista (0,0)
def convertir_coord(coord):
    fila = ord(coord[0].upper()) - 65
    columna = int(coord[1]) - 1
    return fila, columna
# Ejecuta un disparo sobre el tablero del oponente
def disparar(tablero, tablero_disparos, coord, jugador):
    fila, columna = convertir_coord(coord)
    if tablero[fila][columna] == 1:
        print(f"{jugador} hizo ¡Tocado!")
        tablero_disparos[fila][columna] = 3  # Marca como tocado
        tablero[fila][columna] = 0           # Elimina el barco
    elif tablero_disparos[fila][columna] in [2, 3]:
        print("Ya disparaste ahí.")
    else:
        print(f"{jugador} disparó al agua.")
        tablero_disparos[fila][columna] = 2  # Marca como fallo
# Verifica si aún quedan barcos en un tablero
def quedan_barcos(tablero):
    for fila in tablero:
        if 1 in fila:
            return True
    return False
#  Guarda la puntuación del ganador junto con la fecha y hora actual
def guardar_puntuacion(nombre):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formato legible
    with open("puntuaciones.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} ganó la partida el {ahora}\n")
# Función principal del juego
def jugar():
    print("=== Batalla Naval ===\n")
    # Reglas y símbolos del juego
    print("=== Reglas del Juego ===")
    print("1. El tablero es de 4 filas (A-D) y 2 columnas (1-2).")
    print("2. Cada jugador tiene 3 barcos escondidos.")
    print("3. En cada turno puedes disparar una vez.")
    print("4. Gana quien hunda todos los barcos del oponente.\n")
    
    print("Símbolos del tablero:")
    print("   · → Agua o zona no disparada")
    print("   ■ → Barco propio")
    print("   ○ → Agua (fallaste)")
    print("   X → Tocado (impacto en barco)\n")

    # Selección del modo de juego
    print("1. Jugar contra la CPU")
    print("2. Jugar contra otro jugador")
    modo = input("Selecciona modo (1 o 2): ")
    # --- Modo 1: Jugador vs CPU ---
    if modo == "1":
        nombre = input("Tu nombre: ")
        tablero_jugador = crear_tablero()
        tablero_cpu = crear_tablero()
        disparos_jugador = crear_tablero()
        disparos_cpu = crear_tablero()
        colocar_barcos(tablero_jugador)
        colocar_barcos(tablero_cpu)
        turno = 1
        while True:
            print(f"\n--- Turno {turno} ---")
            print("Tu tablero:")
            mostrar_tablero(tablero_jugador)
            print("\nTablero de disparos:")
            mostrar_tablero(disparos_jugador)
            # Turno del jugador
            while True:
                coord = input("Dispara (ej. A1): ")
                if coord_valida(coord):
                    break
                print("Coordenada inválida. Intenta de nuevo.")
            disparar(tablero_cpu, disparos_jugador, coord, nombre)
            # Verificar si ganó el jugador
            if not quedan_barcos(tablero_cpu):
                print("\n=== FIN DEL JUEGO ===")
                print(f"¡{nombre} gana!")
                guardar_puntuacion(nombre)
                break
            # Turno de la CPU
            while True:
                fila = random.randint(0, FILAS - 1)
                columna = random.randint(0, COLUMNAS - 1)
                if disparos_cpu[fila][columna] == 0:
                    break
            coord_cpu = chr(65 + fila) + str(columna + 1)
            print(f"La CPU dispara a {coord_cpu}")
            disparar(tablero_jugador, disparos_cpu, coord_cpu, "CPU")
            # Verificar si ganó la CPU
            if not quedan_barcos(tablero_jugador):
                print("\n=== FIN DEL JUEGO ===")
                print("¡La CPU gana!")
                guardar_puntuacion("CPU")
                break
            turno += 1
    # --- Modo 2: Jugador vs Jugador ---
    elif modo == "2":
        nombre1 = input("Nombre del Jugador 1: ")
        nombre2 = input("Nombre del Jugador 2: ")
        tablero1 = crear_tablero()
        tablero2 = crear_tablero()
        disparos1 = crear_tablero()
        disparos2 = crear_tablero()
        colocar_barcos(tablero1)
        colocar_barcos(tablero2)
        turno = 1
        while True:
            print(f"\n--- Turno {turno} ---")
            # Turno del Jugador 1
            print(f"{nombre1}, este es tu turno")
            mostrar_tablero(disparos1)
            while True:
                coord = input("Dispara (ej. A1): ")
                if coord_valida(coord):
                    break
                print("Coordenada inválida. Intenta de nuevo.")
            disparar(tablero2, disparos1, coord, nombre1)
            if not quedan_barcos(tablero2):
                print("\n=== FIN DEL JUEGO ===")
                print(f"¡{nombre1} gana!")
                guardar_puntuacion(nombre1)
                break
            # Turno del Jugador 2
            print(f"\n{nombre2}, este es tu turno")
            mostrar_tablero(disparos2)
            while True:
                coord = input("Dispara (ej. A1): ")
                if coord_valida(coord):
                    break
                print("Coordenada inválida. Intenta de nuevo.")
            disparar(tablero1, disparos2, coord, nombre2)

            if not quedan_barcos(tablero1):
                print("\n=== FIN DEL JUEGO ===")
                print(f"¡{nombre2} gana!")
                guardar_puntuacion(nombre2)
                break
            turno += 1
    else:
        print("Opción inválida. Saliendo del juego.")
jugar()