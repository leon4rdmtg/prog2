import getpass

print("Bienvenido al juego del ahorcado lógico con listas!")
print("Debes descubrir qué números hay en la lista secreta de 5 elementos.")
print("Pero no puedes verla directamente. En cada turno puedes hacer una pregunta en forma de código Python.")
print("Ejemplos: len(lista_secreta), lista_secreta[2], lista_secreta[0] > 10")
print("Cuando creas tener la lista completa escribe 'adivinar'")
print("--------------------------------------------------------")

while True:
    try:
        # Ingreso oculto de la lista secreta
        entrada = getpass.getpass("🔐 Ingresa la lista secreta (5 números separados por comas, oculto): ")
        lista_secreta = [int(x.strip()) for x in entrada.split(",")]

        if len(lista_secreta) != 5 or any(num < 0 or num > 99 for num in lista_secreta):
            print("⚠️ La lista debe contener 5 números entre 0 y 99.")
            continue
    except ValueError:
        print("⚠️ Ingresa una lista válida de números.")
        continue

    while True:
        instruccion = input(">>> Escribe tu instrucción (o 'adivinar'): ")
        if instruccion.strip().lower() == "adivinar":
            intento = input("Escribe tu intento de lista (separa por comas): ")
            try:
                intento_lista = [int(x.strip()) for x in intento.split(",")]
                if intento_lista == lista_secreta:
                    print("¡Felicidades! Has adivinado la lista secreta. La lista secreta era:", lista_secreta)
                    break
                else:
                    print("Lo siento, esa no es la lista secreta. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Asegúrate de ingresar números separados por comas.")
        else:
            try:
                resultado = eval(instruccion, {"lista_secreta": lista_secreta})
                print("resultado:", resultado)
            except Exception as e:
                print("Error en la instrucción:", e)

