from functools import reduce
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    return 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))
# Pruebas
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(6) == 720
print("¡Pruebas de factoriales pasaron!")
# Solicita un número al usuario
try:
    numero = int(input("Ingrese un número entero para calcular su factorial: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
    print("Fin del programa--------------Nicodemus Berny Quiroga Gonzáles")
except ValueError as e:
    print("Error:", e)
except Exception:
    print("Por favor, ingrese un número entero válido.")
