# Ejercicio 2: Implementación de Búsqueda Binaria
def busqueda_binaria(lista_ordenada, clave):
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio] == clave:
            return medio  # Clave encontrada
        elif clave > lista_ordenada[medio]:
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda
    return -1  # Clave no encontrada
# 🧪 Casos de prueba con assert
lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("\nProbando busqueda_binaria...")
assert busqueda_binaria(lista_ordenada, 23) == 5
assert busqueda_binaria(lista_ordenada, 91) == 9  # Último
assert busqueda_binaria(lista_ordenada, 2) == 0   # Primero
assert busqueda_binaria(lista_ordenada, 3) == -1  # No existe
assert busqueda_binaria(lista_ordenada, 100) == -1  # Fuera de rango (mayor)
print("¡Pruebas para busqueda_binaria pasaron! ")
print ("fin del programa --- jose alejandro zabala roemero")