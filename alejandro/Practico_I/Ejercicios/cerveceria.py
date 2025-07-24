def crear_nombre_cerveceria():
    print("🍺 Bienvenido al generador de nombres para tu cervecería 🍺")

    palabra1 = input("🔤 Ingresa la primera palabra: ").strip()
    palabra2 = input("🔤 Ingresa la segunda palabra: ").strip()

    # Op 1: Palabras unidas
    nombre_completo = palabra1 + palabra2

    # Op2: Combinar 3 letras de cada palabra
    parte1 = palabra1[:3] if len(palabra1) >= 3 else palabra1
    parte2 = palabra2[:3] if len(palabra2) >= 3 else palabra2
    nombre_corto = parte1 + parte2

    print("\n ¡Felicidades! Aquí tienes dos ideas para tu cervecería:\n")
    print(f" Nombre combinado: {nombre_completo}")
    print(f" Nombre corto (3+3 letras): {nombre_corto}")

crear_nombre_cerveceria()
print ("----fin del porgrama---- Jose Alejandro Zabala Romero")