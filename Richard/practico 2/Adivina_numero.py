numero_secreto = 7
while True:
    var = int(input("Adivina el número: "))

    if var < numero_secreto:
        print("Demaciado Bajo")
    elif var > numero_secreto:
        print("Demaciado Alto")
    else:
        print("Correcto! el número secreto es: ",numero_secreto)
        break  

print("--- Fin del programa --- Richard Hurtado" )
assert numero_secreto == 7