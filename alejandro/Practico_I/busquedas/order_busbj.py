def ordenamiento_burbuja(lista):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo de burbuja.
    Modifica la lista original (in-place) y también la retorna por conveniencia.
    """
    n = len(lista)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return lista
if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_burbuja(numeros)
    print("Después Ordenamiento Burbuja:", numeros)
# --- Pruebas burbuja ---
lista1 = [6, 3, 8, 2, 5]
ordenamiento_burbuja(lista1)
assert lista1 == [2, 3, 5, 6, 8]
lista2 = [1, 2, 3, 4, 5]
ordenamiento_burbuja(lista2)
assert lista2 == [1, 2, 3, 4, 5]
lista3 = [5, 4, 3, 2, 1]
ordenamiento_burbuja(lista3)
assert lista3 == [1, 2, 3, 4, 5]
lista4 = [5, 1, 4, 2, 8, 5, 2]
ordenamiento_burbuja(lista4)
assert lista4 == [1, 2, 2, 4, 5, 5, 8]
assert ordenamiento_burbuja([]) == []
assert ordenamiento_burbuja([42]) == [42]
print("¡Todas las pruebas ordenamiento burbuja pasaron! ✅")
print("JOSE ALEJANDRO ZABALA ROMERO - FIN PROGRAMA ORDENAMIENTO BURBUJA")
# ALGORITMO DE INSERCIÓN
def ordenamiento_insercion(lista):
    """
    Ordena la lista in-place usando el algoritmo de inserción.
    Retorna la misma lista por conveniencia.
    """
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion_actual = i
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        lista[posicion_actual] = valor_actual
    return lista
# --- Pruebas inserción ---
lista1 = [6, 3, 8, 2, 5]
print("Antes:", lista1)
ordenamiento_insercion(lista1)
print("Después Ordenamiento Inserción:", lista1)
assert lista1 == [2, 3, 5, 6, 8]
lista2 = [1, 2, 3, 4, 5]
print("Antes:", lista2)
ordenamiento_insercion(lista2)
print("Después Ordenamiento Inserción:", lista2)
assert lista2 == [1, 2, 3, 4, 5]
lista3 = [5, 4, 3, 2, 1]
ordenamiento_insercion(lista3)
assert lista3 == [1, 2, 3, 4, 5]
lista4 = [5, 1, 4, 2, 8, 5, 2]
ordenamiento_insercion(lista4)
assert lista4 == [1, 2, 2, 4, 5, 5, 8]
assert ordenamiento_insercion([]) == []
assert ordenamiento_insercion([42]) == [42]
print("¡Todas las pruebas del ordenamiento por inserción pasaron! ✅")
print("JOSE ALEJANDRO ZABALA ROMERO - FIN PROGRAMA ORDENAMIENTO INSERCIÓN")
