matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 1. Inicialización
sumas_por_fila = []
# 2. Iteración Exterior (por fila)
for fila in matriz:
    # 3a. Inicializa acumulador para esta fila
    acumulador_fila = 0
    # 3b y 3c. Suma cada elemento de la fila
    for elemento in fila:
        acumulador_fila += elemento
    # 4. Guardar suma de la fila
    sumas_por_fila.append(acumulador_fila)
# 5. Resultado final
print("Suma por filas:", sumas_por_fila)
print("\nFin del programa ----- Leonardo Montenegro")