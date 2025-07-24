def heapificar(lista, tamano_heap, indice_raiz):
  """ Asegura que el subárbol con raíz en el índice dado cumpla la propiedad de Max Heap. """
  mayor = indice_raiz
  hijo_izquierdo = 2 * indice_raiz + 1
  hijo_derecho = 2 * indice_raiz + 2
  if hijo_izquierdo < tamano_heap and lista[hijo_izquierdo] > lista[mayor]:
      mayor = hijo_izquierdo
  if hijo_derecho < tamano_heap and lista[hijo_derecho] > lista[mayor]:
      mayor = hijo_derecho
  if mayor != indice_raiz:
      lista[indice_raiz], lista[mayor] = lista[mayor], lista[indice_raiz]
      heapificar(lista, tamano_heap, mayor)
def ordenar_por_heap(lista):
  """ Ordena la lista utilizando el algoritmo Heap Sort. """
  n = len(lista)
  # Construir el Max Heap
  for i in range(n // 2 - 1, -1, -1):
      heapificar(lista, n, i)
  # Extraer elementos del heap uno por uno
  for i in range(n - 1, 0, -1):
      lista[0], lista[i] = lista[i], lista[0]
      heapificar(lista, i, 0)
#  PRUEBAS CON ASSERTS (TESTING)
# Prueba 1: Lista desordenada
numeros1 = [12, 11, 13, 5, 6, 7]
ordenar_por_heap(numeros1)
assert numeros1 == sorted(numeros1), f" Error en números1: {numeros1}"
# Prueba 2: Lista ya ordenada
numeros2 = [1, 2, 3, 4, 5]
ordenar_por_heap(numeros2)
assert numeros2 == [1, 2, 3, 4, 5], f" Error en números2: {numeros2}"
# Prueba 3: Lista en orden inverso
numeros3 = [9, 8, 7, 6, 5]
ordenar_por_heap(numeros3)
assert numeros3 == [5, 6, 7, 8, 9], f" Error en números3: {numeros3}"
# Prueba 4: Lista con elementos repetidos
numeros4 = [3, 1, 2, 3, 1]
ordenar_por_heap(numeros4)
assert numeros4 == sorted(numeros4), f" Error en números4: {numeros4}"
# Prueba 5: Lista con un solo elemento
numeros5 = [42]
ordenar_por_heap(numeros5)
assert numeros5 == [42], f" Error en números5: {numeros5}"
# Prueba 6: Lista vacía
numeros6 = []
ordenar_por_heap(numeros6)
assert numeros6 == [], f" Error en números6: {numeros6}"
print(" Todas las pruebas pasaron correctamente.")
print("Fin del programa----Jose Alejandro Zabala Romero")