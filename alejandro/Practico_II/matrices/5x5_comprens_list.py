print("\nMatriz 5x5 con ceros (usando comprensión de listas):")
matriz_comp = [[0 for _ in range(5)] for _ in range(5)]
for fila in matriz_comp:
    for elemento in fila:
        print(elemento, end="\t")
    print()
print("\nFin del programa Jose Alejandro Zabala Romero")