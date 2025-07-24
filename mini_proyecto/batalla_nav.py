import random
import os

# Tamaño del tablero
TAMANO = 5
NUM_BARCOS = 3

def crear_tablero():
    return [['~' for _ in range(TAMANO)] for _ in range(TAMANO)]

def imprimir_tablero(tablero, ocultar=False):
    print("  " + " ".join([str(i) for i in range(TAMANO)]))
    for i in range(TAMANO):
        fila = []
        for j in range(TAMANO):
            celda = tablero[i][j]
            if ocultar and celda == 'B':
                fila.append('~')
            else:
                fila.append(celda)
        print(str(i) + " " + " ".join(fila))

def colocar_barcos(tablero):
    barcos = 0
    while barcos < NUM_BARCOS:
        fila = random.randint(0, TAMANO - 1)
        col = random.randint(0, TAMANO - 1)
        if tablero[fila][col] == '~':
            tablero[fila][col] = 'B'
            barcos += 1
def disparar(tablero, fila, col):
    if tablero[fila][col] == 'B':
        tablero[fila][col] = 'X'
        return "¡Impacto!"
    elif tablero[fila][col] == '~':
        tablero[fila][col] = 'O'
        return "Agua..."
    elif tablero[fila][col] in ['X', 'O']:
        return "Ya disparaste ahí."
def contar_barcos(tablero):
    return sum(fila.count('B') for fila in tablero)

# Tableros
tablero_jugador = crear_tablero()
tablero_cpu = crear_tablero()
tablero_cpu_visible = crear_tablero()

# Colocar barcos
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_cpu)

# Juego principal
turno = 0
while True:
    os.system("clear")  # Usa "cls" si estás en Windows

    print("=== Batalla Naval ===")
    print("Tu tablero:")
    imprimir_tablero(tablero_jugador)
    print("\nTablero enemigo (oculto):")
    imprimir_tablero(tablero_cpu_visible, ocultar=True)

    # Turno del jugador
    print("\n--- Tu turno ---")
    try:
        fila = int(input("Ingresa fila (0-4): "))
        col = int(input("Ingresa columna (0-4): "))
        if 0 <= fila < TAMANO and 0 <= col < TAMANO:
            resultado = disparar(tablero_cpu, fila, col)
            print(resultado)
            if resultado == "¡Impacto!":
                tablero_cpu_visible[fila][col] = 'X'
            elif resultado == "Agua...":
                tablero_cpu_visible[fila][col] = 'O'
        else:
            print("¡Coordenadas fuera del tablero!")
            continue
    except ValueError:
        print("Entrada inválida.")
        continue

    if contar_barcos(tablero_cpu) == 0:
        print("\n¡Ganaste! Has hundido todos los barcos enemigos.")
        break

    input("\nPresiona Enter para que dispare la CPU...")

    # Turno de la CPU
    while True:
        fila_cpu = random.randint(0, TAMANO - 1)
        col_cpu = random.randint(0, TAMANO - 1)
        if tablero_jugador[fila_cpu][col_cpu] in ['~', 'B']:
            break

    resultado_cpu = disparar(tablero_jugador, fila_cpu, col_cpu)
    print(f"La CPU disparó a ({fila_cpu}, {col_cpu}): {resultado_cpu}")

    if contar_barcos(tablero_jugador) == 0:
        print("\n¡Perdiste! La CPU hundió todos tus barcos.")
        break

    input("\nPresiona Enter para continuar al siguiente turno...")