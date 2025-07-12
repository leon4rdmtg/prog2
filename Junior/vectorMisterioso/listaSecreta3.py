import getpass

# ===================== ETAPA 1: INGRESO DE LISTA SECRETA OCULTA ========================
print("👨‍🏫 Ingreso de la lista secreta (NO visible para los estudiantes)")

# Paso 1: Definir la longitud
while True:
    try:
        cantidad = int(input("¿Cuántos elementos tendrá la lista secreta?: "))
        if cantidad < 1:
            print("⚠️ Debes ingresar al menos un número.")
        else:
            break
    except ValueError:
        print("⚠️ Por favor, ingresa un número entero válido.")

# Paso 2: Ingreso oculto uno por uno
lista_secreta = []

for i in range(cantidad):
    while True:
        try:
            try:
                entrada = getpass.getpass(f"Ingrese el número secreto #{i + 1} (oculto): ")
            except Exception:
                print("⚠️ Entrada oculta no compatible. Usando entrada visible.")
                entrada = input(f"Ingrese el número secreto #{i + 1} (visible): ")
            numero = int(entrada)
            lista_secreta.append(numero)
            break
        except ValueError:
            print("⚠️ Ingresa un número entero válido.")

print(f"\n✅ Lista secreta de {cantidad} elementos cargada correctamente.\n")

# ===================== ETAPA 2: INSTRUCCIONES PARA EL JUEGO ========================
print("🕵️‍♀️ ¡Bienvenidos al juego del Ahorcado Lógico con Listas!")
print(f"La lista secreta tiene {len(lista_secreta)} elementos.")
print("En cada turno puedes hacer una 'pregunta' en forma de código Python.")
print("Ejemplos: len(lista_secreta), lista_secreta[2], lista_secreta[0] > 10")
print("Cuando creas tener la lista completa, escribe: adivinar")
print("--------------------------------------------------------------")

# ===================== ETAPA 3: BUCLE DE JUEGO ========================
while True:
    instruccion = input(">>> Escribe tu instrucción (o 'adivinar'): ").strip().lower()

    if instruccion == "adivinar":
        intento = input("🧠 Escribe tu intento de lista (separa por comas): ")
        try:
            intento_lista = [int(x.strip()) for x in intento.split(",")]

            if intento_lista == lista_secreta:
                print("🎉 ¡Correcto! Has descubierto la lista secreta.")
                break
            else:
                print("❌ Esa no es la lista correcta.")
                aciertos = 0
                for i in range(len(lista_secreta)):
                    if i < len(intento_lista):
                        if intento_lista[i] == lista_secreta[i]:
                            print(f"✅ Posición {i}: correcto ({intento_lista[i]})")
                            aciertos += 1
                        else:
                            print(f"❌ Posición {i}: incorrecto (tuviste {intento_lista[i]}, se esperaba otro número)")
                    else:
                        print(f"⚠️ Faltó ingresar un número en la posición {i}")
                print(f"🔎 Aciertos totales: {aciertos} de {len(lista_secreta)}")
        except ValueError:
            print("⚠️ Error: asegúrate de ingresar solo números separados por comas.")

    else:
        try:
            # Evaluar la instrucción del alumno en un entorno controlado
            resultado = eval(instruccion, {"lista_secreta": lista_secreta})
            print("Resultado:", resultado)
        except Exception as e:
            print("⚠️ Error en tu instrucción:", e)
