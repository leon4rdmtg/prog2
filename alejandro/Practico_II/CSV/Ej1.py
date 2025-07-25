import csv
import os
# -------- PARTE 1: GUARDAR EL INVENTARIO EN CSV --------
# Lista del inventario original
inventario = [ {"producto": "Manzanas", "precio": 0.5, "stock": 100},
    {"producto": "Bananas", "precio": 0.3, "stock": 80},
    {"producto": "Naranjas", "precio": 0.6, "stock": 60}]
# Encabezados (claves de los diccionarios)
encabezados = ["producto", "precio", "stock"]
# Guardar en archivo CSV
nombre_archivo = "inventario.csv"
with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados)
    escritor_csv.writeheader()
    escritor_csv.writerows(inventario)
print(" Inventario guardado exitosamente en 'inventario.csv'.")
# -------- PARTE 2: CARGAR EL INVENTARIO DESDE CSV --------
# Lista vacía para cargar el contenido
inventario_cargado_csv = []
# Leer el archivo CSV
with open(nombre_archivo, mode='r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        # Convertimos tipos correctamente
        producto = fila["producto"]
        precio = float(fila["precio"])
        stock = int(fila["stock"])
        # Añadimos a la lista cargada
        producto_dic = {  "producto": producto,
                          "precio": precio,
                           "stock": stock }
        inventario_cargado_csv.append(producto_dic)
# Mostrar el contenido cargado
print("\n📦 Inventario cargado desde CSV:")
for item in inventario_cargado_csv:
    print(item)
print("\n--- Fin del programa ---- Jose Alejandro Zabala Romero")