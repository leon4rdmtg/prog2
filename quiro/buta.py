filas = 4
columnas = 5
precio_asiento = 25  # Bs
total_butacas = filas * columnas

# Crear matriz de butacas disponibles (True = libre, False = ocupada)
butacas = [[True for _ in range(columnas)] for _ in range(filas)]

def mostrar_butacas():
    print("\nEstado actual de la sala (✔ = libre, ✘ = ocupado):")
    for i in range(filas):
        for j in range(columnas):
            print("✔" if butacas[i][j] else "✘", end=" ")
        print(f" <- Fila {i+1}")
    print("Columna:  1  2  3  4  5\n")

def comprar_butaca():
    total_compra = 0
    butacas_compradas = []
    try:
        n = int(input("¿Cuántas butacas deseas comprar? "))
        if n <= 0:
            print("Debes ingresar un número mayor que 0.")
            return
        disponibles = sum(row.count(True) for row in butacas)
        if n > disponibles:
            print("No hay suficientes butacas disponibles.")
            return

        for i in range(n):
            mostrar_butacas()
            print(f"Selecciona la butaca #{i+1}")
            fila = int(input("Fila (1-4): ")) - 1
            columna = int(input("Columna (1-5): ")) - 1

            if 0 <= fila < filas and 0 <= columna < columnas:
                if butacas[fila][columna]:
                    butacas[fila][columna] = False
                    butacas_compradas.append((fila + 1, columna + 1))
                    total_compra += precio_asiento
                else:
                    print("Esa butaca ya está ocupada. Elige otra.")
                    i -= 1  # repetir la misma iteración
            else:
                print("Butaca fuera de rango. Intenta de nuevo.")
                i -= 1

        print("\nResumen de compra:")
        for b in butacas_compradas:
            print(f" - Fila {b[0]}, Asiento {b[1]}")
        print(f"Total a pagar: {total_compra} Bs")
    except ValueError:
        print("Entrada no válida. Intenta de nuevo.")

def cambiar_asiento():
    try:
        fila_actual = int(input("Fila actual (1-4): ")) - 1
        columna_actual = int(input("Columna actual (1-5): ")) - 1
        if butacas[fila_actual][columna_actual]:
            print("Esa butaca no está ocupada.")
            return

        # Liberar la butaca actual
        butacas[fila_actual][columna_actual] = True

        # Elegir nueva butaca
        mostrar_butacas()
        fila_nueva = int(input("Nueva fila (1-4): ")) - 1
        columna_nueva = int(input("Nueva columna (1-5): ")) - 1

        if butacas[fila_nueva][columna_nueva]:
            butacas[fila_nueva][columna_nueva] = False
            print(f"Has cambiado a la fila {fila_nueva + 1}, asiento {columna_nueva + 1}.")
        else:
            print("La nueva butaca ya está ocupada. No se hizo el cambio.")
            # Reocupar la anterior si falla
            butacas[fila_actual][columna_actual] = False
    except ValueError:
        print("Entrada inválida.")

# Programa principal
while True:
    print("\n--- Menú ---")
    print("1. Ver butacas")
    print("2. Comprar butacas")
    print("3. Cambiar asiento")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_butacas()
    elif opcion == "2":
        comprar_butaca()
    elif opcion == "3":
        cambiar_asiento()
    elif opcion == "4":
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
