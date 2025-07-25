# 1. Una matriz de 3x3 llamada teclado que representa un teclado numérico
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 2. Imprimir la matriz completa
print("Matriz original:")
for fila in teclado:
    print(fila)
# 3. Mostrar valores específicos usando doble índice
print(f"\nNúmero en el centro: {teclado[1][1]}")         # fila 1, columna 1 → 5
print(f"Número en la esquina inferior derecha: {teclado[2][2]}")  # fila 2, columna 2 → 9
# 4. Modificar el número en la esquina superior izquierda (fila 0, columna 0)
teclado[0][0] = 0
# 5. Imprimir la matriz nuevamente para ver el cambio
print("\nMatriz modificada:")
for fila in teclado:
    print(fila)
print("\nFin del programa ----- leonardo montenegro")