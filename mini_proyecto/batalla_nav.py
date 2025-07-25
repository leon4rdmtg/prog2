import random
AGUA = "🌊"
FALLO = "❌"
BARCO = "🚢"
ACIERTA = "🔥"
TAM_TABLERO = 3
ARCHIVO_PUNTUACIONES = "puntuaciones.txt"
def crear_tablero():
    return [[AGUA for _ in range(TAM_TABLERO)] for _ in range(TAM_TABLERO)]
def imprimir_tablero(tablero):
    print("  " + " ".join([str(i) for i in range(TAM_TABLERO)]))
    for idx, fila in enumerate(tablero):
        print(str(idx) + " " + " ".join(fila))
def colocar_barcos_aleatoriamente(tablero):
    barcos = 3
    while barcos > 0:
        fila = random.randint(0, TAM_TABLERO - 1)
        col = random.randint(0, TAM_TABLERO - 1)
        if tablero[fila][col] == AGUA:
            tablero[fila][col] = BARCO
            barcos -= 1
def disparar(tablero, visibles, fila, col):
    if tablero[fila][col] == BARCO:
        visibles[fila][col] = ACIERTA
        tablero[fila][col] = ACIERTA
        print("¡Tocado! 🎯")
        return True
    else:
        visibles[fila][col] = FALLO
        print("¡Agua! 🌊")
        return False
def turno_jugador(nombre, tablero, visibles):
    while True:
        try:
            fila = int(input(f"{nombre}, elige fila (0-{TAM_TABLERO - 1}): "))
            col = int(input(f"{nombre}, elige columna (0-{TAM_TABLERO - 1}): "))
            if 0 <= fila < TAM_TABLERO and 0 <= col < TAM_TABLERO and visibles[fila][col] == AGUA:
                return disparar(tablero, visibles, fila, col)
            else:
                print("Coordenadas inválidas o ya usadas.")
        except ValueError:
            print("Por favor, ingresa números válidos.")
def turno_cpu(tablero, visibles):
    print("Turno de la CPU 🤖")
    while True:
        fila = random.randint(0, TAM_TABLERO - 1)
        col = random.randint(0, TAM_TABLERO - 1)
        if visibles[fila][col] == AGUA:
            resultado = disparar(tablero, visibles, fila, col)
            return resultado
def contar_aciertos(tablero):
    return sum(fila.count(ACIERTA) for fila in tablero)
def guardar_puntuacion(nombre, aciertos):
    with open(ARCHIVO_PUNTUACIONES, "a") as f:
        f.write(f"{nombre}:{aciertos}\n")
def mostrar_puntuaciones():
    try:
        with open(ARCHIVO_PUNTUACIONES, "r") as f:
            datos = [line.strip().split(":") for line in f.readlines()]
            datos.sort(key=lambda x: int(x[1]), reverse=True)
            print("🏆 Puntuaciones 🏆")
            for nombre, puntos in datos:
                print(f"{nombre}: {puntos} aciertos")
    except FileNotFoundError:
        print("No hay puntuaciones registradas aún.")
def ver_reglas():
    print("""
📜 Reglas del Juego - Batalla Naval

- El tablero es de tamaño 3x3.
- Cada jugador (o CPU) tiene 3 barcos ocultos.
- En tu turno, elige una fila y una columna para disparar.
- Si aciertas, verás un 🔥; si fallas, un ❌.
- Gana quien hunda los 3 barcos del oponente.
- Las puntuaciones se guardan al final de cada partida.
""")
def jugar_vs_jugador():
    nombre1 = input("Nombre del Jugador 1: ")
    nombre2 = input("Nombre del Jugador 2: ")
    tablero1 = crear_tablero()
    visibles1 = crear_tablero()
    colocar_barcos_aleatoriamente(tablero1)
    tablero2 = crear_tablero()
    visibles2 = crear_tablero()
    colocar_barcos_aleatoriamente(tablero2)
    turno = 0
    while True:
        if turno % 2 == 0:
            print(f"\nTurno de {nombre1}")
            imprimir_tablero(visibles2)
            if turno_jugador(nombre1, tablero2, visibles2):
                if contar_aciertos(tablero2) == 3:
                    print(f"\n🎉 ¡{nombre1} gana! 🎉")
                    guardar_puntuacion(nombre1, 3)
                    break
        else:
            print(f"\nTurno de {nombre2}")
            imprimir_tablero(visibles1)
            if turno_jugador(nombre2, tablero1, visibles1):
                if contar_aciertos(tablero1) == 3:
                    print(f"\n🎉 ¡{nombre2} gana! 🎉")
                    guardar_puntuacion(nombre2, 3)
                    break
        turno += 1
def jugar_vs_cpu():
    nombre = input("Tu nombre: ")
    tablero_jugador = crear_tablero()
    visibles_cpu = crear_tablero()
    colocar_barcos_aleatoriamente(tablero_jugador)

    tablero_cpu = crear_tablero()
    visibles_jugador = crear_tablero()
    colocar_barcos_aleatoriamente(tablero_cpu)
    turno = 0
    while True:
        if turno % 2 == 0:
            print(f"\n{nombre}, es tu turno")
            imprimir_tablero(visibles_jugador)
            if turno_jugador(nombre, tablero_cpu, visibles_jugador):
                if contar_aciertos(tablero_cpu) == 3:
                    print(f"\n🎉 ¡{nombre} gana! 🎉")
                    guardar_puntuacion(nombre, 3)
                    break
        else:
            if turno_cpu(tablero_jugador, visibles_cpu):
                if contar_aciertos(tablero_jugador) == 3:
                    print("\n💀 ¡La CPU gana! 💀")
                    guardar_puntuacion("CPU", 3)
                    break
        turno += 1
def menu():
    while True:
        print("""
====== Batalla Naval ======
1. Jugar contra otro jugador
2. Jugar contra la CPU
3. Ver puntuaciones
4. Ver reglas del juego
5. Salir
""")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            jugar_vs_jugador()
        elif opcion == "2":
            jugar_vs_cpu()
        elif opcion == "3":
            mostrar_puntuaciones()
        elif opcion == "4":
            ver_reglas()
        elif opcion == "5":
            print("¡Gracias por jugar! 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
menu()