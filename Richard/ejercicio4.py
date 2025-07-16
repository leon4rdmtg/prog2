def clasificador_peliculas(edad):

  if edad < 0:
    return "edad no valida."
  elif edad < 13:
    return "te recomendamos peliculas clasificadas G o PG."
  elif edad < 18:
    return "te recomendamos peliculas clasificadas PG-13."
  else:
    return "puedes ver peliculas clasificadas R."

assert clasificador_peliculas(20) == "puedes ver peliculas clasificadas R.", "Error en la clasificación para edad 20"
assert clasificador_peliculas(15) == "te recomendamos peliculas clasificadas PG-13.", "Error en la clasificación para edad 15"
assert clasificador_peliculas(10) == "te recomendamos peliculas clasificadas G o PG.", "Error en la clasificación para edad 10"
assert clasificador_peliculas(-5) == "edad no valida.", "Error para edad negativa"

print ("pruebas unitarias superadas")

while True:
    try:
        edad = int(input("Introduce tu edad: "))
        resultado = clasificador_peliculas(edad)
        print(resultado)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    continuar = input("¿Quieres clasificar otra edad? (s/n): ").strip().lower()
    if continuar != 's':
        break
    print("Fin del programa----Richard Hurtado")


