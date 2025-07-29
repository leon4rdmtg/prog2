nombre_archivo = "mi_diario.txt"
# Verificamos si el archivo existe; si no, lo creamos vacío
import os
if not os.path.exists(nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        f.write("")
# Pedimos al usuario que escriba su nueva entrada
entrada = input("Escribe tu nueva entrada para el diario:\n")
# Añadimos un separador y la entrada del usuario al archivo en modo añadir ('a')
with open(nombre_archivo, 'a') as diario_file:
    diario_file.write("\n--- Nueva entrada ---\n")
    diario_file.write(entrada + "\n")
print("¡Tu entrada ha sido guardada!")
# Mostrar todo el contenido actualizado
print("\n--- Contenido completo del diario ---")
try:
    with open(nombre_archivo, 'r') as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
print("\n--- Fin del programa ---- Leonardo Montenegro")