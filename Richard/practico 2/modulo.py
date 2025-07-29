import csv

# Datos a guardar en el archivo
datos = [{"nombre": "Alejandro", "edad": 20},
         {"nombre": "Richard", "edad": 22}]
encabezados = ["nombre", "edad"]

# Escritura del archivo CSV
with open("datos.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
    escritor.writeheader()             # Escribe los encabezados: nombre, edad
    escritor.writerows(datos)         # Escribe cada diccionario como una fila

# Lectura del archivo CSV
lista_leida = []
with open("datos.csv", "r", newline="", encoding="utf-8") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila_dict in lector:
        fila_dict['edad'] = int(fila_dict['edad'])  # Convierte edad a entero
        lista_leida.append(fila_dict)

# Mostramos lo leído
print(lista_leida)
print ("fin del programa ---- richard hurtado")