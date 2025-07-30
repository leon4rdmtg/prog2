tareas = []

def mostrar_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def ver_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas):
            estado = "✔️" if tarea["completada"] else "❌"
            print(f"{i + 1}. [{estado}] {tarea['texto']}")

def agregar_tarea():
    texto = input("Ingresa la nueva tarea: ")
    tareas.append({"texto": texto, "completada": False})
    print("✅ Tarea agregada.")

def completar_tarea():
    ver_tareas()
    try:
        i = int(input("Número de tarea a marcar como completada: ")) - 1
        if 0 <= i < len(tareas):
            tareas[i]["completada"] = True
            print("✅ Tarea completada.")
        else:
            print("❌ Número inválido.")
    except:
        print("❌ Entrada inválida.")

def eliminar_tarea():
    ver_tareas()
    try:
        i = int(input("Número de tarea a eliminar: ")) - 1
        if 0 <= i < len(tareas):
            tareas.pop(i)
            print("🗑️ Tarea eliminada.")
        else:
            print("❌ Número inválido.")
    except:
        print("❌ Entrada inválida.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        ver_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida.")



