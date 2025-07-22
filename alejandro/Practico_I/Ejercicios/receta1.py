# Lista de ejemplo
numeros = [5, 12, 3, 9, 20, 7]
# Paso 1: Suposición inicial
if len(numeros) == 0:
    print("La lista está vacía. No se puede encontrar el mayor.")
else:
    mayor_temporal = numeros[0]
    # Paso 2, 3 y 4: Iteración y comparación
    for numero in numeros[1:]:  # comenzamos desde el segundo elemento
        if numero > mayor_temporal:
            mayor_temporal = numero
    # Paso 5: Resultado
    print(f"El número más grande de la lista es: {mayor_temporal}")
print("--- Fin del programa --- jose alejandro zabala romero")