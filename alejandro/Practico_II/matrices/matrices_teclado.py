matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila_actual in matriz:
    for elemento in fila_actual:
        print(elemento, end=" ")
    print()

print()

matriz = [[col + fila * 5 + 1 for col in range(5)] for fila in range(5)]
for fila in matriz:
    print(" ".join(str(elem) for elem in fila))

print()

teclado_numerico = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
                    ['*', '0', '#']]
for fila in teclado_numerico:
    print(" ".join(fila))

print("Fin del Programa ----- Jose Alejandro Zabala Romero")