# Matriz teclado modificada del ejercicio anterior
teclado = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Recorriendo con bucles anidados para imprimir como cuadrícula
print("Teclado en forma de cuadrícula:")
for fila in teclado:
    for elemento in fila:
        print(elemento, end="\t")
    print()
print("\nFin del programa Jose Alejandro Zabala Romero")
