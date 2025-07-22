# Matriz de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 1. Inicialización
num_filas = len(matriz)
num_columnas = len(matriz[0])
sumas_por_columna = [0] * num_columnas  # lista con ceros para cada columna
# 2. Iteración anidada con índices
for i in range(num_filas):
    for j in range(num_columnas):
        # 3. Acumulación por índice
        sumas_por_columna[j] += matriz[i][j]
# 4. Resultado final
print("Suma por columnas:", sumas_por_columna)
print("\nFin del programa ---- Jose Alejandro Zabala Romero")