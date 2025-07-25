import json
# Archivo donde se almacenarán las tareas en formato JSON
ARCHIVO_DE_DATOS = "mis_tareas.json"
# Lista principal de tareas y variable para llevar control del ID único
lista_de_tareas = []
proximo_id_tarea = 1
# Funciones de manejo de archivos
def cargar_tareas():
    """Carga las tareas y el próximo ID desde el archivo JSON.
    Si el archivo no existe o está corrupto, se inicia una lista vacía."""
    global lista_de_tareas, proximo_id_tarea
    try:
        with open(ARCHIVO_DE_DATOS, 'r', encoding="utf-8") as f:
            datos = json.load(f)
            lista_de_tareas = datos.get("tareas", [])
            proximo_id_tarea = datos.get("proximo_id", 1)
        print("✅ Tareas cargadas desde el archivo.")
    except FileNotFoundError:
        print("ℹ Archivo de tareas no encontrado. Se iniciará una lista nueva.")
    except json.JSONDecodeError:
        print("❌ Error: El archivo de datos está corrupto. Se iniciará una lista nueva.")
def guardar_tareas():
    """Guarda la lista de tareas y el próximo ID en el archivo JSON."""
    datos_a_guardar = {
        "tareas": lista_de_tareas,
        "proximo_id": proximo_id_tarea
    }
    with open(ARCHIVO_DE_DATOS, 'w', encoding="utf-8") as f:
        json.dump(datos_a_guardar, f, indent=4, ensure_ascii=False)
    print("✅ Tareas guardadas exitosamente en el archivo.")
# Funciones principales de la app
def mostrar_menu():
    """Muestra las opciones disponibles para el usuario."""
    print("\n--- TO-DO LIST ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("0. Salir")
def ver_tareas():
    """Muestra todas las tareas actuales con su ID y estado (completado o no)."""
    if not lista_de_tareas:
        print("📭 No hay tareas.")
    else:
        for tarea in lista_de_tareas:
            estado = "✔️" if tarea["completada"] else "❌"
            print(f"{tarea['id']}. [{estado}] {tarea['texto']}")
def buscar_tarea_por_id(tid):
    """Busca una tarea en la lista por su ID. Devuelve la tarea o None si no existe."""
    for tarea in lista_de_tareas:
        if tarea["id"] == tid:
            return tarea
    return None
def agregar_tarea():
    """Solicita al usuario el texto de una nueva tarea y la añade con un ID único."""
    global proximo_id_tarea
    texto = input("📝 Ingresa la nueva tarea: ")
    nueva_tarea = {
        "id": proximo_id_tarea,
        "texto": texto,
        "completada": False
    }
    lista_de_tareas.append(nueva_tarea)
    proximo_id_tarea += 1
    print("✅ Tarea agregada.")
def marcar_tarea_completada():
    """Pide un ID y marca la tarea correspondiente como completada si existe."""
    try:
        tid = int(input("🔢 ID de la tarea a completar: "))
        tarea = buscar_tarea_por_id(tid)
        if tarea:
            tarea["completada"] = True
            print("✅ Tarea marcada como completada.")
        else:
            print("❌ No se encontró una tarea con ese ID.")
    except:
        print("❌ Entrada inválida.")
def eliminar_tarea():
    """Elimina una tarea según su ID, manteniendo intactos los IDs de las otras tareas."""
    try:
        tid = int(input("🗑️ ID de la tarea a eliminar: "))
        tarea = buscar_tarea_por_id(tid)
        if tarea:
            lista_de_tareas.remove(tarea)
            print("🗑️ Tarea eliminada.")
            # Los IDs NO se renumeran, se conservan como fueron creados
        else:
            print("❌ No se encontró una tarea con ese ID.")
    except:
        print("❌ Entrada inválida.")
# Bucle principal del programa
# Se cargan las tareas al inicio del programa
cargar_tareas()
# Ciclo principal del menú
while True:
    mostrar_menu()
    opcion = input("👉 Elige una opción: ")
    if opcion == "1":
        ver_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        marcar_tarea_completada()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "0":
        guardar_tareas()  # Se guardan las tareas antes de salir
        print("👋 ¡Hasta pronto!")
        break
    else:
        print("❌ Opción no válida.")