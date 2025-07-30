
def contar_apariciones(lista, elemento_buscar):
    contador = 0
    for elemento in lista:
        if elemento == elemento_buscar:
            contador += 1
    return contador

# Prueba
lista = [3, 5, 3, 2, 3]
valor = 3
print(f"El número {valor} aparece {contar_apariciones(lista, valor)} veces.")


