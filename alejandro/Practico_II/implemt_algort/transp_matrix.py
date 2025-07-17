def transponer_matriz(matriz):
  """
  Esta función recibe una matriz (lista de listas) y devuelve su transpuesta.
  """
  f = len(matriz)              # Paso 1: filas
  c = len(matriz[0]) if f > 0 else 0  # columnas

  matriz_transpuesta = []     # Paso 2: nueva matriz vacía

  for j in range(c):          # Paso 3: recorrer columnas de la original
      nueva_fila = []         # Paso 4a: inicializar nueva fila
      for i in range(f):      # Paso 4b: recorrer filas de la original
          nueva_fila.append(matriz[i][j])  # Paso 4c: añadir elemento
      matriz_transpuesta.append(nueva_fila)  # Paso 5: agregar nueva fila a transpuesta

  return matriz_transpuesta   # Paso 6: devolver resultado final

# Pruebas para verificar que la transposición funciona correctamente
def probar_transposicion():
  print("\nProbando transponer_matriz...")
  # Caso 1: matriz 3x2
  m1 = [[1, 2],
        [3, 4],
        [5, 6]]
  t1 = [[1, 3, 5],
        [2, 4, 6]]
  assert transponer_matriz(m1) == t1
  # Caso 2: matriz 2x2
  m2 = [[7, 8],
        [9, 10]]
  t2 = [[7, 9],
        [8, 10]]
  assert transponer_matriz(m2) == t2
  # Caso borde: matriz vacía
  assert transponer_matriz([]) == []
  print("¡Pruebas para transponer_matriz pasaron! ✅")
# Llamamos a la función de prueba
print("Fin del programa ------Jose Alejandro Zabala Romero")