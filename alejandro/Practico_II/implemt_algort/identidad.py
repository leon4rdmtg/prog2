def es_identidad(matriz):
    num_filas = len(matriz)
    if num_filas == 0:
        return True  # Una matriz vacía es identidad por convención
    for i in range(num_filas):
        if len(matriz[i]) != num_filas:
            return False  # No es cuadrada

    for i in range(num_filas):
        for j in range(num_filas):
            if i == j:
                if matriz[i][j] != 1:
                    return False  # La diagonal debe tener 1
            else:
                if matriz[i][j] != 0:
                    return False  # Fuera de la diagonal debe haber 0
    return True
# =================== PRUEBAS DE LA FUNCIÓN ===================
identidad = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
no_identidad = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]
no_cuadrada = [[1, 0], [0, 1], [0, 0]]
assert es_identidad(identidad) == True
assert es_identidad(no_identidad) == False
assert es_identidad(no_cuadrada) == False
print("Todas las pruebas pasaron correctamente.")
print("Fin del programa ----- leonardo montenegro")