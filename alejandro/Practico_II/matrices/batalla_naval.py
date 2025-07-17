import random
# Tamaño del tablero (por ejemplo 5x5)
FILAS = 5
COLUMNAS = 5
# Crear una matriz con ceros
def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
# Mostrar el tablero en consola
def mostrar_tablero(tablero, ocultar_barcos=False):
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        letra = chr(ord('A') + i)
        fila_mostrar = []
        for celda in fila:
            if ocultar_barcos and celda == 1:
                fila_mostrar.append("0")
            elif celda == 0:
                fila_mostrar.append("0")
            elif celda == 1:
                fila_mostrar.append("1")
            elif celda == 2:
                fila_mostrar.append("X")
            elif celda == 3:
                fila_mostrar.append("*")
        print(letra + " " + " ".join(fila_mostrar))
# Convertir coordenada tipo "A3" a [fila][columna]
def coord_a_indices(coord):
    fila = ord(coord[0].upper()) - ord('A')
    columna = int(coord[1:]) - 1
    return fila, columna
# Colocar barcos aleatoriamente en el tablero
def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            colocados += 1
# Ejecutar un disparo
def disparar(tablero_objetivo, tablero_disparos, coord):
    fila, columna = coord_a_indices(coord)
    if tablero_objetivo[fila][columna] == 1:
        tablero_objetivo[fila][columna] = 2
        tablero_disparos[fila][columna] = 2
        print("¡Tocado!")
    elif tablero_objetivo[fila][columna] in [0, 3]:
        tablero_objetivo[fila][columna] = 3
        tablero_disparos[fila][columna] = 3
        print("Agua...")
    else:
        print("Ya disparaste allí.")
# Comprobar si hay barcos vivos
def quedan_barcos(tablero):
    for fila in tablero:
        if 1 in fila:
            return True
    return False
# Juego principal
def juego():
    print("=== Batalla Naval ===")
    tablero_jugador = crear_tablero()
    tablero_cpu = crear_tablero()
    tablero_disparos_jugador = crear_tablero()
    tablero_disparos_cpu = crear_tablero()
    # Colocar barcos
    colocar_barcos(tablero_jugador, 3)
    colocar_barcos(tablero_cpu, 3)
    turno = 1
    while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_cpu):
        print(f"\n--- Turno {turno} ---")
        print("Tu tablero:")
        mostrar_tablero(tablero_jugador)
        print("Tus disparos:")
        mostrar_tablero(tablero_disparos_jugador)
        # Turno del jugador
        coord = input("Ingresa coordenada para disparar (ej. A3): ")
        disparar(tablero_cpu, tablero_disparos_jugador, coord)
        # Turno del CPU (simplemente al azar)
        while True:
            fila_cpu = random.randint(0, FILAS - 1)
            col_cpu = random.randint(0, COLUMNAS - 1)
            if tablero_jugador[fila_cpu][col_cpu] in [0, 1]:
                break
        coord_cpu = f"{chr(ord('A') + fila_cpu)}{col_cpu + 1}"
        print(f"La CPU dispara a {coord_cpu}")
        disparar(tablero_jugador, tablero_disparos_cpu, coord_cpu)
        turno += 1
    if quedan_barcos(tablero_jugador):
        print("¡Ganaste!")
    else:
        print("La CPU gana.")
    # Nombre al final
    print("\nFin del programa Jose Alejandro Zabala Romero")
# Ejecutar el juego
juego()