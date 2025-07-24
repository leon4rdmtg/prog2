def es_simetrica(matriz):
    num_filas = len(matriz)
    if num_filas == 0:
        return True  # Una matriz vacía es simétrica por convención
    for i in range(num_filas):
        if len(matriz[i]) != num_filas:
            return False  # No es cuadrada
    for i in range(num_filas):
        for j in range(i + 1, num_filas):  # Solo triangular superior
            if matriz[i][j] != matriz[j][i]:
                return False  # Encontramos una diferencia
    return True
# =================== PRUEBAS DE LA FUNCIÓN ===================
sim = [[1, 7, 3], [7, 4, -5], [3, -5, 6]]
no_sim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
no_cuadrada = [[1, 2], [3, 4], [5, 6]]
assert es_simetrica(sim) == True
assert es_simetrica(no_sim) == False
assert es_simetrica(no_cuadrada) == False
print("¡Pruebas para es_simetrica pasaron! ")
print("Fin del programa ----- jose alejandro zabala romero")