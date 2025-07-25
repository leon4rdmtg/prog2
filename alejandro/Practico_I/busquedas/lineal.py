# Ejercicio 1: Implementación de Búsqueda Lineal

def busqueda_lineal(lista, clave):
    # Recorremos la lista usando índices con range
    for i in range(len(lista)):
        if lista[i] == clave:
            return i  # Si encontramos la clave, devolvemos su índice
    return -1  # Si no la encontramos, devolvemos -1
# Casos de prueba con assert
mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]
print("Probando busqueda_lineal...")
assert busqueda_lineal(mi_lista_desordenada, 42) == 2
assert busqueda_lineal(mi_lista_desordenada, 10) == 0  # Al inicio
assert busqueda_lineal(mi_lista_desordenada, 25) == 6  # Al final
assert busqueda_lineal(mi_lista_desordenada, 99) == -1  # No existe
assert busqueda_lineal([], 5) == -1  # Lista vacía
print("¡Pruebas para busqueda_lineal pasaron! ✅")
print ("jose alejandro ---- fin del programa")