numero_secreto = 7
while True:
  var = int(input("Adivina el número secreto: "))

  if var < numero_secreto:
    print("demasiado frio")
  elif var > numero_secreto:
      print("demasiado caliente")
  else:
        print("¡Acertaste! el número secreto es: ", numero_secreto )
        break
print("Fin del programa----Richard hurtado")
assert numero_secreto == 7