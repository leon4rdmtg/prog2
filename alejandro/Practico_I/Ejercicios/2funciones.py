def saludar(nombre_persona):
  """
  Recibe un nombre y devuelve un saludo personalizado (modificada para pruebas).
  """
  mensaje = f"¡Hola, {nombre_persona}! ¡Qué bueno tenerte aquí!"
  return mensaje
def sumar(a, b):
  """
  Recibe dos números y devuelve su suma.
  """
  return a + b
# ===== Pruebas unitarias con assert =====
assert saludar("Jose") == "¡Hola, Jose! ¡Qué bueno tenerte aquí!", "Error en saludo para Jose"
assert saludar("Alejandro") == "¡Hola, Alejandro! ¡Qué bueno tenerte aquí!", "Error en saludo para Alejandro"
assert sumar(2, 3) == 5, "Error: 2 + 3 debe ser 5"
assert sumar(-4, 4) == 0, "Error: -4 + 4 debe ser 0"
print(" Todas las pruebas unitarias pasaron correctamente.\n")
# ===== Llamadas a las funciones =====
print(saludar("Jose"))
print(f"La suma de 7 y 8 es: {sumar(7, 8)}")
print("Fin del programa-------------- Jose Alejandro Zabala Romero")