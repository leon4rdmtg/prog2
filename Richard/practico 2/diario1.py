
nombre_archivo = "mi_diario.txt"

with open(nombre_archivo, 'w') as diario_file:
   
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")

print("Diario guardado correctamente en 'mi_diario.txt'")
print ("fin del programa --- Richard hurtado")