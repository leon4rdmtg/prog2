print("📚 Calculadora de Promedio de 5 Notas")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
n5 = float(input("Nota 5: "))

promedio = (n1 + n2 + n3 + n4 + n5) / 5

print(f"\n📊 Tu promedio es: {promedio:.2f}")

if promedio >= 70:
    print("🎉 ¡Felicidades! Vas bien.")
else:
    print("💪 Ánimo, a seguir esforzándote.")