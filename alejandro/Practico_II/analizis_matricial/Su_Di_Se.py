def sumar_diagonal_secundaria(matriz):
  """
  Esta función recibe una matriz cuadrada y retorna la suma
  de los elementos de su diagonal secundaria (de derecha a izquierda).
  """
  suma = 0
  n = len(matriz)
  for i in range(n):
      suma += matriz[i][n - 1 - i]
  return suma
def probar_suma_diagonal_secundaria():
  print("\nProbando sumar_diagonal_secundaria...")
  m1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
  assert sumar_diagonal_secundaria(m1) == 15  # 3 + 5 + 7
  m2 = [[0, 0, 1],
        [0, 2, 0],
        [3, 0, 0]]
  assert sumar_diagonal_secundaria(m2) == 6  # 1 + 2 + 3
  m3 = [[8]]
  assert sumar_diagonal_secundaria(m3) == 8  # Solo un elemento
  print("¡Pruebas para sumar_diagonal_secundaria pasaron! ✅")
if __name__ == "__main__":
  probar_suma_diagonal_secundaria()
  print("\nFin del programa ----- Jose Alejandro Zabala Romero")