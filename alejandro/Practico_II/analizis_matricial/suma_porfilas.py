def sumar_por_filas(matriz):
  """
  Esta función recibe una matriz (lista de listas)
  y devuelve una lista con la suma de cada fila.
  """
  # Usamos comprensión de listas para sumar cada fila
  return [sum(fila) for fila in matriz]
def probar_suma_por_filas():
  print("\nProbando sumar_por_filas...")
  m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  assert sumar_por_filas(m1) == [6, 15, 24]
  m2 = [[10, 10], [20, 20], [30, 30]]
  assert sumar_por_filas(m2) == [20, 40, 60]
  assert sumar_por_filas([]) == []
  print("¡Pruebas para sumar_por_filas pasaron! ✅")
if __name__ == "__main__":
  probar_suma_por_filas()
  print("\nFin del programa ---- Jose Alejandro Zabala Romero")