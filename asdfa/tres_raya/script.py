def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    print("  0   1   2")
    for i, fila in enumerate(tablero):
        print(i, " | ".join(fila))
        if i < 2:
            print("  ---------")

def hay_ganador(tablero, jugador):
    # Revisar filas, columnas y diagonales
    for i in range(3):
        if all([casilla == jugador for casilla in tablero[i]]) or \
           all([tablero[j][i] == jugador for j in range(3)]):
            return True
    if (tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador) or \
       (tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador):
        return True
    return False

def tablero_lleno(tablero):
    return all(casilla != " " for fila in tablero for casilla in fila)

def jugar():
    tablero = crear_tablero()
    jugador = "X"

    while True:
        mostrar_tablero(tablero)
        print(f"Turno del jugador {jugador}")
        
        try:
            fila = int(input("Ingresa la fila (0, 1 o 2): "))
            columna = int(input("Ingresa la columna (0, 1 o 2): "))
        except ValueError:
            print("Entrada no válida. Usa números.")
            continue

        if 0 <= fila <= 2 and 0 <= columna <= 2:
            if tablero[fila][columna] == " ":
                tablero[fila][columna] = jugador

                if hay_ganador(tablero, jugador):
                    mostrar_tablero(tablero)
                    print(f"¡Felicidades! El jugador {jugador} ha ganado.")
                    break
                elif tablero_lleno(tablero):
                    mostrar_tablero(tablero)
                    print("¡Empate!")
                    break

                jugador = "O" if jugador == "X" else "X"
            else:
                print("Esa casilla ya está ocupada. Intenta otra.")
        else:
            print("Coordenadas fuera de rango. Intenta con 0, 1 o 2.")

if __name__ == "_main_":
    jugar()






