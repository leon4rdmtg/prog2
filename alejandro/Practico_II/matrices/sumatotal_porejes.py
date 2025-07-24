matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 1. Inicialización
acumulador_total = 0
# 2. Iteración Anidada
for fila in matriz:
    # 3. Recorremos cada elemento en la fila actual
    for elemento in fila:
        # 4. Acumulación
        acumulador_total += elemento
# 5. Resultado
print(f"La suma total de todos los elementos es: {acumulador_total}")
print("\nFin del programa ---- Jose Alejandro Zabala Romero")