# Definimos una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("=== Opción 1: Recorriendo con índices ===")
num_filas = len(matriz)
num_columnas = len(matriz[0])

for i in range(num_filas):  # Bucle exterior: recorre las filas
    for j in range(num_columnas):  # Bucle interior: recorre las columnas
        elemento = matriz[i][j]
        print(f"Elemento en ({i},{j}) es {elemento}")

print("\n=== Opción 2: Recorriendo por elementos (más Pythonico) ===")
for fila_actual in matriz:  # Bucle exterior: cada fila completa
    for elemento in fila_actual:  # Bucle interior: cada número en esa fila
        print(elemento, end=' ')
    print()  # Salto de línea después de imprimir una fila completa

