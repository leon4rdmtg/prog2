# ==== PASO 1: Crear estructura base ====
tareas = []
id_actual = 1
# ==== PASO 2: Función para agregar tarea ====
def agregar_tarea(descripcion, prioridad="media"):
    global id_actual
    nueva_tarea = {
        "id": id_actual,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "completada": False
    }
    tareas.append(nueva_tarea)
    print(f" Tarea '{descripcion}' añadida con éxito.")
    id_actual += 1
# ==== PASO 3: Función para mostrar tareas ====
def mostrar_tareas():
    print("\n---  LISTA DE TAREAS ---")
    if not tareas:
        print(" No hay tareas registradas.")
    else:
        for tarea in tareas:
            estado = "✅" if tarea["completada"] else "⬜"
            print(f"{estado} ID: {tarea['id']} | {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")
# Prueba paso 3:
agregar_tarea("Estudiar para el examen de Cálculo")
agregar_tarea("Hacer las compras", prioridad="alta")
mostrar_tareas()
# ==== PASO 4: Función para buscar tarea por ID ====
def buscar_tarea_por_id(id_busqueda):
    for tarea in tareas:
        if tarea["id"] == id_busqueda:
            return tarea
    return None
# Prueba paso 4:
tarea_encontrada = buscar_tarea_por_id(1)
if tarea_encontrada:
    print(f"\n🔍 Búsqueda exitosa: {tarea_encontrada['descripcion']}")
else:
    print("\n❌ Búsqueda fallida: Tarea no encontrada.")
tarea_fantasma = buscar_tarea_por_id(99)
if not tarea_fantasma:
    print("✅ Búsqueda de tarea inexistente funcionó correctamente.")
# ==== PASO 5: Función para marcar como completada ====
def marcar_tarea_completada(id_tarea):
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea:
        tarea["completada"] = True
        print(f"✅ Tarea '{tarea['descripcion']}' marcada como completada.")
    else:
        print("❌ Error: No se encontró la tarea con ese ID.")
# ==== PASO 6: Función para eliminar tarea ====
def eliminar_tarea(id_tarea):
    global tareas
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea:
        tareas = [t for t in tareas if t["id"] != id_tarea]
        print(f"✅ Tarea '{tarea['descripcion']}' eliminada.")
    else:
        print("❌ Error: No se encontró la tarea con ese ID.")
# Prueba paso 6:
mostrar_tareas()
marcar_tarea_completada(1)
mostrar_tareas()  # La tarea 1 debería mostrarse como completada
eliminar_tarea(2)
mostrar_tareas()  # La tarea 2 ya no debería aparecer
marcar_tarea_completada(99)  # ID que no existe
# ==== PASO 7: Menú interactivo ====
def menu():
    while True:
        print("\n==== MENÚ TO-DO LIST ====")
        print("1. Agregar nueva tarea")
        print("2. Mostrar todas las tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            descripcion = input("Descripción de la nueva tarea: ")
            prioridad = input("Prioridad (alta, media, baja): ").lower()
            agregar_tarea(descripcion, prioridad)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            try:
                id_tarea = int(input("ID de la tarea a completar: "))
                marcar_tarea_completada(id_tarea)
            except ValueError:
                print("❌ Ingresa un número válido.")
        elif opcion == "4":
            try:
                id_tarea = int(input("ID de la tarea a eliminar: "))
                eliminar_tarea(id_tarea)
            except ValueError:
                print("❌ Ingresa un número válido.")
        elif opcion == "0":
            print("¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")
menu()
print("Fin del programa ----- jose alejandro zabala romero")