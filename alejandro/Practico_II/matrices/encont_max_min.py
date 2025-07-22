# Matriz de ejemplo (cuadrada 3x3)
matriz = [
    [5, 2, 9],
    [1, 8, 3],
    [4, 7, 6]
]
# 1. Suposición inicial (verificando que la matriz no esté vacía)
if not matriz or not matriz[0]:
    print("La matriz está vacía.")
else:
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    # Asumimos el primer elemento como máximo temporal
    mayor_temporal = matriz[0][0]
    # 2 y 3. Iteración anidada para recorrer todos los elementos
    for i in range(num_filas):
        for j in range(num_columnas):
            if matriz[i][j] > mayor_temporal:
                mayor_temporal = matriz[i][j]
    print(f"El valor máximo en la matriz es: {mayor_temporal}")
    # Si la matriz es cuadrada (N x N)
    if num_filas == num_columnas:
        N = num_filas
        diagonal_principal = []
        diagonal_secundaria = []
        # Recorrido de la diagonal principal y secundaria
        for i in range(N):
            diagonal_principal.append(matriz[i][i])
            diagonal_secundaria.append(matriz[i][N - 1 - i])
        print("Diagonal principal:", diagonal_principal)
        print("Diagonal secundaria:", diagonal_secundaria)
print("\nFin del programa Jose Alejandro Zabala Romero")