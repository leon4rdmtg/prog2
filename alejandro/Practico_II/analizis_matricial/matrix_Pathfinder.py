def hay_camino(matriz):
  """
  Determina si existe un camino desde la esquina superior izquierda (0, 0)
  hasta la esquina inferior derecha (N-1, N-1) en una matriz.
  0 = camino libre, 1 = pared.
  Usa búsqueda en profundidad (DFS).
  """
  if not matriz or matriz[0][0] == 1:
      return False
  n = len(matriz)
  visitado = [[False]*n for _ in range(n)]

  def dfs(x, y):
      if x < 0 or x >= n or y < 0 or y >= n:
          return False
      if matriz[x][y] == 1 or visitado[x][y]:
          return False
      if (x, y) == (n-1, n-1):
          return True
      visitado[x][y] = True

      # Explorar en las 4 direcciones
      return (dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1))
  return dfs(0, 0)
# ------------------ Pruebas ------------------
print("Pruebas del camino en la matriz:")
matriz1 = [
  [0, 1, 0],
  [0, 0, 0],
  [1, 1, 0]
]
print(hay_camino(matriz1))  # True, hay camino desde (0,0) a (2,2)
matriz2 = [
  [0, 1, 1],
  [1, 1, 1],
  [1, 1, 0]
]
print(hay_camino(matriz2))  # False, bloqueado
matriz3 = [
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 0]
]
print(hay_camino(matriz3))  # True
print( "Fin del programa --- Jose Alejandro Zabala Romero")