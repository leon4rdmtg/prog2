
def invertir_lista(lista_original):
    lista_invertida = []
    for i in range(len(lista_original) - 1, -1, -1):
        lista_invertida.append(lista_original[i])
    return lista_invertida

# Prueba
lista = [1, 2, 3, 4]
print(f"Lista original: {lista}")
print(f"Lista invertida: {invertir_lista(lista)}")




