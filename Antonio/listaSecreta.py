import getpass

print("Bienvenido al juego del ahorcado logico con listas!")
print("Debes decubrir que numeros hay en la lista secreta de 5 elementos.")
print("Pero no puedes verla directamente. En cada turno pueder hacer una pregunta rn forma de codigo python")
print("Ejemplos: len(lista_secreta), lista_secreta[2], lista_secreta[0] > 10")
print("Cuando creas tener la lista completa escribe 'adivinar'")
print("--------------------------------------------------------")


while True:

  try:
    # Ingreso oculto del número secreto
    entrada = getpass.getpass("🔐 Ingresa el número secreto (oculto, máx 99): ")
    lista_secreta = int(entrada)

    if lista_secreta > 99 or lista_secreta < 0:
        print("⚠️ El número debe estar entre 0 y 99.")
        continue
  except ValueError:
    print("⚠️ Ingresa un número válido.")
    continue


  while True:
    instruccion = input(">>> Escribe tu instruccion (o 'adivinar'): ")
    if instruccion.strip().lower() == "adivinar":
      intento = input("Escribe tu intento de lista (separa por comas): ")
      try:
        intento_lista = [int (x.strip()) for x in intento.split(",")]
        if intento_lista == lista_secreta:
          print("¡Felicidades! Has adivinado la lista secreta.")
          break
        else:
          print("Lo siento, esa no es la lista secreta. Intenta de nuevo.")
      except ValueError:
        print("Entrada no valida. Asegurate de ingresar numeros separados por comas.")
    else:
      try:
        resultado = eval(instruccion, {"lista_secreta": lista_secreta})
        print("resultado:", resultado)
      except Exception as e:
        print("Error en la instruccion:", e)

