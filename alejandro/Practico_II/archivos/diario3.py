# Definimos el nombre del archivo
nombre_archivo = "mi_diario.txt"
# Escritura inicial (modo 'w' borra todo y escribe)
with open(nombre_archivo, 'w') as diario_file:
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")
print("Diario guardado correctamente.")
# Añadimos nuevas entradas sin borrar las anteriores (modo 'a')
print("\nAñadiendo nuevas entradas al diario...")
with open(nombre_archivo, 'a') as diario_file:
    diario_file.write("\n--- Entrada del 20 de Junio de 2025 ---\n")
    diario_file.write("El modo 'a' es genial para no perder datos.\n")
    diario_file.write("Ahora mi diario puede crecer cada día.\n")
print("¡Nuevas entradas guardadas!")
# Lectura línea por línea con manejo de errores (Opción B)
print("\n--- Contenido del diario (línea por línea) ---")
try:
    with open(nombre_archivo, 'r') as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
print("\n--- Fin del programa ---- Leonardo Montenegro")