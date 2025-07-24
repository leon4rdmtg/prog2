total_butacas = 20
# Crear una lista de butacas disponibles (1 a 20)
butacas = list(range(1, total_butacas + 1))
print(f"Hay {total_butacas} butacas disponibles:")
print(butacas)

# Pedir al usuario cuántas butacas quiere comprar
try:
    n = int(input("¿Cuántas butacas deseas comprar? "))

    if n <= 0:
        print("Debes ingresar un número mayor que 0.")
    elif n > total_butacas:
        print("No hay suficientes butacas disponibles.")
    else:
        # Marcar las primeras n butacas como ocupadas
        butacas_ocupadas = butacas[:n]
        butacas_libres = butacas[n:]

        print(f"\nHas comprado {n} butaca(s): {butacas_ocupadas}")
        print(f"Butacas restantes ({len(butacas_libres)}): {butacas_libres}")
except ValueError:
    print("Por favor, ingresa un número válido.")