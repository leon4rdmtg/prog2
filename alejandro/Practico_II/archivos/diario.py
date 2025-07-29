# 1. Definimos el nombre del archivo
nombre_archivo = "mi_diario.txt"
# 2. Abrimos el archivo en modo escritura ('w')
with open(nombre_archivo, 'w') as diario_file:
    # 3. Escribimos varias entradas en el archivo
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")
# 4. Confirmamos que el archivo fue escrito
print("Diario guardado correctamente en 'mi_diario.txt'")
print ("fin del programa --- Richard hurtado")