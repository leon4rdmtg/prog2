# Definimos el nombre del archivo
nombre_archivo = "mi_diario.txt"
# Escritura
with open(nombre_archivo, 'w') as diario_file:
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. Qué miedo!\n")
print("Diario guardado correctamente.")
# Lectura (línea por línea con manejo de errores)
print("\n--- Contenido del diario (línea por línea) ---")
try:
    with open(nombre_archivo, 'r') as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
print("\n--- Fin del programa ---- Leonardo Montenegro")