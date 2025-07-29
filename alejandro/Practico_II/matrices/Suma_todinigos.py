matriz = [
    [10, 2, 3, 4, 5],
    [6, 20, 8, 9, 10],
    [11, 12, 30, 14, 15],
    [16, 17, 18, 40, 20],
    [21, 22, 23, 24, 50]
]
# Suma total
suma = sum(sum(fila) for fila in matriz)
print("Suma total:", suma)
# Suma por filas
print("Suma por filas:")
for i, fila in enumerate(matriz):
    print(f"Fila {i}: {sum(fila)}")
# Suma por columnas
print("Suma por columnas:")
for j in range(5):
    col = sum(matriz[i][j] for i in range(5))
    print(f"Columna {j}: {col}")
# Máximo y mínimo
todos = [num for fila in matriz for num in fila]
print("Máximo:", max(todos))
print("Mínimo:", min(todos))
print("Diagonal principal:")
print(' '.join(str(matriz[i][i]) for i in range(5)))
print("Diagonal secundaria:")
print(' '.join(str(matriz[i][4 - i]) for i in range(5)))
print("Fin del programa --- Richard hurtado")