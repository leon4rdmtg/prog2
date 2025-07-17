def sumar_diagonal_principal(matriz):
  """
  Esta función recibe una matriz cuadrada (misma cantidad de filas y columnas)
  y retorna la suma de los elementos en su diagonal principal.
  """
  return sum(matriz[i][i] for i in range(len(matriz)))
def probar_suma_diagonal_principal():
  print("\nProbando sumar_diagonal_principal...")
  m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  assert sumar_diagonal_principal(m1) == 15  # 1 + 5 + 9
  m2 = [[10, 0], [0, 20]]
  assert sumar_diagonal_principal(m2) == 30  # 10 + 20
  m3 = [[5]]
  assert sumar_diagonal_principal(m3) == 5   # Solo un elemento en la diagonal
  print("¡Pruebas para sumar_diagonal_principal pasaron! ✅")
if __name__ == "__main__":
  probar_suma_diagonal_principal()
  print("\nFin del programa ---- Jose Alejandro Zabala Romero")