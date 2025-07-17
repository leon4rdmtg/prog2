# Función que suma los elementos de la diagonal secundaria de una matriz cuadrada
def sumar_diagonal_secundaria(matriz):
    """
    Recibe una matriz cuadrada (misma cantidad de filas y columnas)
    y devuelve la suma de los elementos en la diagonal secundaria.
    La diagonal secundaria va desde la esquina superior derecha
    hasta la esquina inferior izquierda.
    Por ejemplo, en una matriz 3x3:
    [[a, b, c],
     [d, e, f],
     [g, h, i]]
    La diagonal secundaria está en las posiciones: (0,2), (1,1), (2,0)
    y su suma sería: c + e + g
    """
    n = len(matriz)
    return sum(matriz[i][n - 1 - i] for i in range(n))
# Funciones de prueba para validar que sumar_diagonal_secundaria funciona correctamente
def probar_suma_diagonal_secundaria():
    print("\nProbando sumar_diagonal_secundaria...")
    # Caso 1: matriz 3x3 normal
    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    # Diagonal secundaria: 3 + 5 + 7 = 15
    assert sumar_diagonal_secundaria(m1) == 15
    # Caso 2: matriz 2x2
    m2 = [[10, 1],
          [2, 20]]
    # Diagonal secundaria: 1 + 2 = 3
    assert sumar_diagonal_secundaria(m2) == 3

    # Caso 3: matriz 1x1
    m3 = [[42]]
    # Solo hay un elemento: 42
    assert sumar_diagonal_secundaria(m3) == 42
    print("¡Pruebas para sumar_diagonal_secundaria pasaron! ✅")
# Llamamos a la función de prueba
probar_suma_diagonal_secundaria()
print("Fin del programa --- Jose Alejandro Zabala Romero")