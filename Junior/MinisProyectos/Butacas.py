# 1. Crear sala llena de 'L'
def crear_sala(filas, columnas):
    return [['L' for _ in range(columnas)] for _ in range(filas)]

# 2. Mostrar la sala visualmente
def mostrar_sala(sala):
    print("\nSala de Cine:")
    print("   " + " ".join([f"{i+1:2}" for i in range(len(sala[0]))]))
    for idx, fila in enumerate(sala):
        print(f"{idx+1:2} " + "  ".join(fila))
    print()

# 3. Ocupar asiento si está libre y las coordenadas son válidas
def ocupar_asiento(sala, fila, columna):
    filas_totales = len(sala)
    columnas_totales = len(sala[0])
    if 0 <= fila < filas_totales and 0 <= columna < columnas_totales:
        if sala[fila][columna] == 'L':
            sala[fila][columna] = 'O'
            print("✅ Asiento reservado con éxito.")
            return True
        else:
            print("❌ El asiento ya está ocupado.")
            return False
    else:
        print("❌ Coordenadas fuera del rango.")
        return False

# 4. Contar cuántos asientos libres quedan
def contar_asientos_libres(sala):
    return sum(fila.count('L') for fila in sala)

# 5. Contar cuántos asientos ocupados hay
def contar_asientos_ocupados(sala):
    return sum(fila.count('O') for fila in sala)


# PROGRAMA PRINCIPAL
def main():
    PRECIO_ENTRADA = 30  # Precio de cada entrada en Bs
    sala = crear_sala(5, 8)  # 5 filas, 8 columnas

    while True:
        mostrar_sala(sala)
        print("🎫 MENÚ:")
        print("1. Ocupar un asiento")
        print("2. Ver cuántos asientos libres quedan")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                fila = int(input("Ingrese la fila (1-5): ")) - 1
                columna = int(input("Ingrese la columna (1-8): ")) - 1
                ocupar_asiento(sala, fila, columna)
            except ValueError:
                print("❌ Por favor, ingrese números válidos.")
        elif opcion == "2":
            libres = contar_asientos_libres(sala)
            print(f"🟩 Hay {libres} asientos libres.\n")
        elif opcion == "0":
            ocupados = contar_asientos_ocupados(sala)
            total = ocupados * PRECIO_ENTRADA
            print(f"🎟️ Entradas reservadas: {ocupados}")
            print(f"💰 Total a pagar: {total} Bs")
            print("👋 ¡Gracias por usar el sistema de cine!")
            break
        else:
            print("❌ Opción no válida. Intente otra vez.")


main()
