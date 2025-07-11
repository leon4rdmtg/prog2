def invertir_lista(lista):
  return lista[::-1]

mi_lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(mi_lista)
print("Lista original:", mi_lista)
print("Lista invertida:", lista_invertida)

print("\nProbando invertir_lista con slicing...")

lista_prueba = [1, 2, 3, 4, 5]
lista_resultante = invertir_lista(lista_prueba)

assert lista_resultante == [5, 4, 3, 2, 1], "❌ Error en inversión con slicing"
assert lista_prueba == [1, 2, 3, 4, 5], "❌ ¡La lista original fue modificada!"
assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
assert invertir_lista([]) == []

print("¡Pruebas con slicing pasaron! ✅")
