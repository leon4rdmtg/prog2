def sumar_total_matriz(matriz):
    """
    Suma todos los elementos de una matriz (lista de listas).
    Retorna 0 si la matriz está vacía o si las filas están vacías.
    """
    if not matriz:
        return 0
    # Suma todos los elementos con comprensión de listas
    return sum(elemento for fila in matriz if fila for elemento in fila)
def probar_suma_total():
    print("Probando sumar_total_matriz...")
    m1 = [[1, 2, 3], [4, 5, 6]]
    assert sumar_total_matriz(m1) == 21
    m2 = [[-1, 0, 1], [10, -5, 5]]
    assert sumar_total_matriz(m2) == 10
    assert sumar_total_matriz([[]]) == 0
    assert sumar_total_matriz([]) == 0
    assert sumar_total_matriz([[42]]) == 42
    assert sumar_total_matriz([[], [1, 2, 3], []]) == 6
    print("¡Pruebas para sumar_total_matriz pasaron! ")
if __name__ == "__main__":
    probar_suma_total()
    print("\nFin del programa ---- Junior Pacajes Banegas")