# Lista inicial de comidas favoritas
comidas_favoritas = ["Pizza", "Tacos", "Sushi", "Hamburguesa", "Empanadas"]

def mostrar_comidas():
    print("\n🍽️ Lista de comidas favoritas:")
    for i, comida in enumerate(comidas_favoritas, start=1):
        print(f"{i}. {comida}")

def modificar_comida():
    mostrar_comidas()
    try:
        opcion = int(input("\n🔧 ¿Qué número de comida deseas modificar?: "))
        if 1 <= opcion <= len(comidas_favoritas):
            nueva_comida = input("✏️ Escribe la nueva comida: ")
            comidas_favoritas[opcion - 1] = nueva_comida
            print("\n✅ Comida modificada con éxito.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Debes ingresar un número.")

def menu():
    while True:
        print("\n=== MENÚ ===")
        print("1. Ver lista de comidas favoritas")
        print("2. Modificar una comida")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_comidas()
        elif opcion == "2":
            modificar_comida()
        elif opcion == "3":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")

menu()


