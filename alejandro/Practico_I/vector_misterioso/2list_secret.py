# ===================== ETAPA 1: INGRESO DE LISTA SECRETA ========================
print("👨‍🏫 Ingreso de la lista secreta (NO visible para los estudiantes)")
while True:
    try:
        cantidad = int(input("¿Cuántos elementos tendrá la lista secreta?: "))
        if cantidad >= 1:
            break
        print("⚠️ Debes ingresar al menos un elemento.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")
while True:
    entrada = input(f"👉 Ingresa {cantidad} números separados por coma: ")
    try:
        lista_secreta = [int(x.strip()) for x in entrada.split(",")]
        if len(lista_secreta) == cantidad:
            break
        print(f"⚠️ Debes ingresar {cantidad} elementos. Ingresaste {len(lista_secreta)}.")
    except ValueError:
        print("⚠️ Ingresa solo números válidos separados por comas.")
print(f"\n✅ Lista secreta de {cantidad} elementos cargada correctamente.\n")
# ===================== ETAPA 2: INSTRUCCIONES ========================
print("🕵️‍♀️ ¡Bienvenidos al juego del Ahorcado Lógico con Listas!")
print(f"La lista secreta tiene {cantidad} elementos.")
print("Puedes hacer preguntas como: len(lista_secreta), lista_secreta[2], lista_secreta[0] > 10")
print("Cuando creas saber la lista completa, escribe: adivinar")
print("--------------------------------------------------------------")
# ===================== ETAPA 3: BUCLE DE JUEGO ========================
while True:
    instruccion = input(">>> Instrucción (o 'adivinar'): ").strip().lower()

    if instruccion == "adivinar":
        intento = input("🧠 Tu intento de lista (separa por comas): ")
        try:
            intento_lista = [int(x.strip()) for x in intento.split(",")]
            if intento_lista == lista_secreta:
                print("🎉 ¡Correcto! Has descubierto la lista secreta.")
                break
            print("❌ Esa no es la lista correcta.")
            aciertos = sum(
                1 for i, val in enumerate(intento_lista)
                if i < len(lista_secreta) and val == lista_secreta[i]
            )
            for i in range(len(lista_secreta)):
                if i >= len(intento_lista):
                    print(f"⚠️ Faltó ingresar un número en la posición {i}")
                elif intento_lista[i] == lista_secreta[i]:
                    print(f"✅ Posición {i}: correcto ({intento_lista[i]})")
                else:
                    print(f"❌ Posición {i}: incorrecto (tuviste {intento_lista[i]})")
            print(f"🔎 Aciertos totales: {aciertos} de {len(lista_secreta)}")
        except ValueError:
            print("⚠️ Ingresa solo números separados por comas.")
    else:
        try:
            resultado = eval(instruccion, {"lista_secreta": lista_secreta})
            print("Resultado:", resultado)
        except Exception as e:
            print("⚠️ Error en tu instrucción:", e)
print("fin del programa ---- Jose Alejandro Zabala Romero")
