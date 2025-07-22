print("\nMatriz 5x5 con ceros (usando bucles):")
matriz_ceros = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz_ceros.append(fila)
for fila in matriz_ceros:
    for elemento in fila:
        print(elemento, end="\t")
    print()
print("\nFin del programa Jose Alejandro Zabala Romero")
