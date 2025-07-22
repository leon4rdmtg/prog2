def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    matriz_transpuesta = []
    for j in range(num_columnas):  # Recorremos columnas de la original
        nueva_fila = []
        for i in range(num_filas):  # Recorremos filas de la original
            nueva_fila.append(matriz[i][j])
        matriz_transpuesta.append(nueva_fila)
    return matriz_transpuesta
# Prueba 1: Matriz 2x3
m1 = [[1, 2, 3], [4, 5, 6]]
t1 = transponer_matriz(m1)
assert t1 == [[1, 4], [2, 5], [3, 6]]
print("Prueba 1 (2x3) pasada!")
# Prueba 2: Matriz cuadrada 2x2
m2 = [[7, 8], [9, 10]]
t2 = transponer_matriz(m2)
assert t2 == [[7, 9], [8, 10]]
print("Prueba 2 (2x2) pasada!")
# Prueba 3: Matriz 3x1
m3 = [[1], [2], [3]]
t3 = transponer_matriz(m3)
assert t3 == [[1, 2, 3]]
print("Prueba 3 (3x1) pasada!")
# Prueba 4: Matriz 1x3
m4 = [[10, 20, 30]]
t4 = transponer_matriz(m4)
assert t4 == [[10], [20], [30]]
print("Prueba 4 (1x3) pasada!")
m5 = []
t5 = transponer_matriz(m5)
assert t5 == []
print("Prueba 5 (matriz vacía) pasada!")
print("Fin del programa ----- Jose Alejandro Zabala Romero")