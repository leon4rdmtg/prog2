import json
import os

# --- Funciones de persistencia ---
def guardar_datos(sala, precios, archivo="datos_cine.json"):
    with open(archivo, "w") as f:
        json.dump({"sala": sala, "precios": precios}, f)

def cargar_datos(archivo="datos_cine.json"):
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            datos = json.load(f)
            return datos["sala"], datos["precios"]
    else:
        return crear_sala(5, 8), []

# --- Funciones de cine ---
def crear_sala(filas, columnas):
    return [['L' for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    print("\nSala de Cine:")
    print("   " + " ".join([f"{i + 1:2}" for i in range(len(sala[0]))]))
    for idx, fila in enumerate(sala):
        print(f"{idx + 1:2} " + "  ".join(fila))
    print()

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

def contar_asientos_libres(sala):
    return sum(fila.count('L') for fila in sala)

def reiniciar_sala(sala):
    for i in range(len(sala)):
        for j in range(len(sala[0])):
            sala[i][j] = 'L'

# --- Programa principal ---
def main():
    sala, precios_entradas = cargar_datos()

    while True:
        mostrar_sala(sala)
        print("🎫 MENÚ:")
        print("1. Ocupar varios asientos")
        print("2. Ver cuántos asientos libres quedan")
        print("3. Reiniciar sala")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                cantidad = int(input("¿Cuántos asientos desea reservar?: "))
                for i in range(cantidad):
                    print(f"\n➡️ Asiento {i + 1}:")
                    while True:
                        try:
                            fila = int(input("Ingrese la fila (1-5): ")) - 1
                            columna = int(input("Ingrese la columna (1-8): ")) - 1
                            if ocupar_asiento(sala, fila, columna):
                                break
                        except ValueError:
                            print("❌ Ingrese valores válidos para fila y columna.")
                    while True:
                        try:
                            precio = float(input("Ingrese el precio para este asiento (Bs): "))
                            precios_entradas.append(precio)
                            guardar_datos(sala, precios_entradas)
                            break
                        except ValueError:
                            print("❌ Ingrese un número válido para el precio.")
            except ValueError:
                print("❌ Por favor, ingrese un número válido.")

        elif opcion == "2":
            libres = contar_asientos_libres(sala)
            print(f"🟩 Hay {libres} asientos libres.\n")

        elif opcion == "3":
            confirmar = input("¿Seguro que desea reiniciar la sala? (s/n): ").lower()
            if confirmar == "s":
                reiniciar_sala(sala)
                precios_entradas.clear()
                guardar_datos(sala, precios_entradas)
                print("🔄 Sala reiniciada correctamente.\n")

        elif opcion == "0":
            total = sum(precios_entradas)
            print(f"🎟️ Entradas reservadas: {len(precios_entradas)}")
            print(f"💰 Total a pagar: {total:.2f} Bs")
            input("Presione ENTER para salir...")
            break

        else:
            print("❌ Opción no válida. Intente otra vez.")

# Ejecutar programa
if __name__ == "__main__":
    main()
