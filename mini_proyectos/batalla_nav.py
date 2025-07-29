import random
from datetime import datetime
# Tamaño del tablero y cantidad de barcos
FILAS = 5
COLUMNAS = 5
BARCOS = 3
# tablero vacío
def crear_tablero(): 
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]
# barcos aleatorios
def colocar_barcos(tablero): 
    barcos_colocados = 0
    while barcos_colocados < BARCOS:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            barcos_colocados += 1
 #  tablero con líneas estilo cuadrícula
def mostrar_tablero(tablero):
    print("    " + "   ".join(str(i + 1) for i in range(COLUMNAS)))
    print("  +" + "---+" * COLUMNAS)
    for i, fila in enumerate(tablero):
        linea = chr(65 + i) + " |"
        for celda in fila:
            if celda == 0:
                linea += "   |"
            elif celda == 1:
                linea += " ■ |"
            elif celda == 2:
                linea += " ○ |"
            elif celda == 3:
                linea += " X |"
        print(linea)
        print("  +" + "---+" * COLUMNAS)
# Validar coordenadas
def coord_valida(coord):
    if len(coord) < 2 or len(coord) > 3:
        return False
    fila = coord[0].upper()
    columna = coord[1:]
    return fila in "ABCDE" and columna.isdigit() and 1 <= int(columna) <= COLUMNAS
# Pide una coordenada válida al jugador
def pedir_coordenada():
    while True:
        coord = input("Dispara (ej. A1): ")
        if coord_valida(coord):
            return coord
        print("Coordenada inválida. Intenta de nuevo.")
# Convierte A1 → (0, 0)
def convertir_coord(coord):
    fila = ord(coord[0].upper()) - 65
    columna = int(coord[1:]) - 1
    return fila, columna
# Ejecuta un disparo
def disparar(tablero, tablero_disparos, coord, jugador):
    fila, columna = convertir_coord(coord)
    if tablero[fila][columna] == 1:
        print(f"{jugador} hizo ¡Tocado!")
        tablero_disparos[fila][columna] = 3  
        tablero[fila][columna] = 0           
        return True
    elif tablero_disparos[fila][columna] in [2, 3]:
        print("Ya disparaste ahí.")
        return False
    else:
        print(f"{jugador} disparó al agua.")
        tablero_disparos[fila][columna] = 2  
        return False
# Verifica si quedan barcos
def quedan_barcos(tablero):
    for fila in tablero:
        if 1 in fila:
            return True
    return False
# Guarda la puntuación
def guardar_puntuacion(nombre):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("puntuaciones.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} ganó la partida el {ahora}\n")
# Función principal
def jugar():
    print("=== Batalla Naval ===\n")
    print("=== Reglas del Juego ===")
    print("1. El tablero es de 5 filas (A-E) y 5 columnas (1-5).")
    print("2. Cada jugador tiene 3 barcos escondidos.")
    print("3. En cada turno puedes disparar una vez.")
    print("4. Gana quien hunda todos los barcos del oponente.\n")

    print("Símbolos del tablero:")
    print("    (espacio en blanco) → Zona no disparada")
    print("   ■ → Barco propio")
    print("   ○ → Agua (fallaste)")
    print("   X → Tocado (impacto en barco)\n")
    print("1. Jugar contra la CPU")
    print("2. Jugar contra otro jugador")
    modo = input("Selecciona modo (1 o 2): ")
    if modo == "1":
        # Modo contra CPU
        nombre = input("Tu nombre: ")
        tablero_jugador = crear_tablero()
        tablero_cpu = crear_tablero()
        disparos_jugador = crear_tablero()
        disparos_cpu = crear_tablero()
        colocar_barcos(tablero_jugador)
        colocar_barcos(tablero_cpu)
        turno = 1
        # Contadores de tocados para jugador y CPU
        tocados_jugador = 0
        tocados_cpu = 0
        while True:
            print(f"\n--- Turno {turno} ---")
            print("Tu tablero:")
            mostrar_tablero(tablero_jugador)
            print("\nTablero de disparos:")
            mostrar_tablero(disparos_jugador)
            # Mostrar conteo de tocados
            print(f"Tocados {nombre}: {tocados_jugador}  |  Tocados CPU: {tocados_cpu}")
            # Turno jugador
            coord = pedir_coordenada()
            if disparar(tablero_cpu, disparos_jugador, coord, nombre):
                tocados_jugador += 1
            if not quedan_barcos(tablero_cpu):
                print("\n=== FIN DEL JUEGO ===")
                print(f"¡{nombre} gana!")
                guardar_puntuacion(nombre)
                break
            # Turno CPU: elige coordenada aleatoria no disparada
            while True:
                fila = random.randint(0, FILAS - 1)
                columna = random.randint(0, COLUMNAS - 1)
                if disparos_cpu[fila][columna] == 0:
                    break
            coord_cpu = chr(65 + fila) + str(columna + 1)
            print(f"La CPU dispara a {coord_cpu}")
            if disparar(tablero_jugador, disparos_cpu, coord_cpu, "CPU"):
                tocados_cpu += 1

            if not quedan_barcos(tablero_jugador):
                print("\n=== FIN DEL JUEGO ===")
                print("¡La CPU gana!")
                guardar_puntuacion("CPU")
                break
            turno += 1

    elif modo == "2":
        # Modo dos jugadores
        nombre1 = input("Nombre del Jugador 1: ")
        nombre2 = input("Nombre del Jugador 2: ")
        tablero1 = crear_tablero()
        tablero2 = crear_tablero()
        disparos1 = crear_tablero()
        disparos2 = crear_tablero()
        colocar_barcos(tablero1)
        colocar_barcos(tablero2)
        turno = 1
        # Contadores de tocados para ambos jugadores
        tocados_1 = 0
        tocados_2 = 0
        while True:
            print(f"\n--- Turno {turno} ---")
            print(f"{nombre1}, este es tu turno")
            mostrar_tablero(disparos1)
            # Mostrar conteo de tocados
            print(f"Tocados {nombre1}: {tocados_1}  |  Tocados {nombre2}: {tocados_2}")
            coord = pedir_coordenada()
            if disparar(tablero2, disparos1, coord, nombre1):
                tocados_1 += 1
            if not quedan_barcos(tablero2):
                print("\n=== FIN DEL JUEGO ===")
                print(f"¡{nombre1} gana!")
                guardar_puntuacion(nombre1)
                break
            print(f"\n{nombre2}, este es tu turno")
            mostrar_tablero(disparos2)
            print(f"Tocados {nombre1}: {tocados_1}  |  Tocados {nombre2}: {tocados_2}")
            coord = pedir_coordenada()
            if disparar(tablero1, disparos2, coord, nombre2):
                tocados_2 += 1
            if not quedan_barcos(tablero1):
                print("\n=== FIN DEL JUEGO ===")
                print(f"¡{nombre2} gana!")
                guardar_puntuacion(nombre2)
                break
            turno += 1
    else:
        print("Opción inválida. Saliendo del juego.")
# Ejecuta el juego
jugar()