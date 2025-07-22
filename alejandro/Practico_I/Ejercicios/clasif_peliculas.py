def clasificar_peliculas(edad):
    if edad < 0:
        return "Edad no válida."
    elif edad < 13:
        return "Te recomendamos películas clasificadas G o PG."
    elif edad < 18:
        return "Puedes ver películas clasificadas PG-13."
    else:
        return "¡Puedes ver películas clasificadas R!"
# ===== Pruebas unitarias =====
assert clasificar_peliculas(20) == "¡Puedes ver películas clasificadas R!", "Error para edad 20"
assert clasificar_peliculas(15) == "Puedes ver películas clasificadas PG-13.", "Error para edad 15"
assert clasificar_peliculas(10) == "Te recomendamos películas clasificadas G o PG.", "Error para edad 10"
assert clasificar_peliculas(-5) == "Edad no válida.", "Error para edad negativa"
print(" Pruebas unitarias superadas.")
# ===== Verificador interactivo de edades =====
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        resultado = clasificar_peliculas(edad)
        print(f" {resultado}")
    except ValueError:
        print(" Debes ingresar un número entero válido.")
        continue

    continuar = input("¿Deseas verificar otra edad? (Y/N): ").strip().lower()
    if continuar != 'y':
        break
print("--- Fin del programa --- Jose Alejandro Zabala Romero")

