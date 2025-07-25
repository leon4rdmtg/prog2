# ============================
#  EJERCICIO 1: Estructura base del sistema (menú + estructura de tareas)
# ============================
def mostrar_menu():
    print("\n📋 MENÚ DE TAREAS:")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("0. Salir")
# ============================
#  EJERCICIO 2: Uso de listas de diccionarios para las tareas
# ============================
tareas = []
proximo_id = 1
# ============================
#  EJERCICIO 3: Persistencia con archivo JSON
# ============================

import json
import os

def cargar_tareas():
    global tareas, proximo_id
    if os.path.exists("mis_tareas.json"):
        with open("mis_tareas.json", "r") as archivo:
            datos = json.load(archivo)
            tareas = datos.get("tareas", [])
            proximo_id = datos.get("proximo_id", 1)
            
def guardar_tareas():
    with open("mis_tareas.json", "w") as archivo:
        json.dump({
            "tareas": tareas,
            "proximo_id": proximo_id
        }, archivo, indent=4)


#  Funciones adicionales
def ver_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    for tarea in tareas:
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{tarea['id']}. {estado} {tarea['texto']}")
def agregar_tarea():
    global proximo_id
    texto = input("Ingresa la nueva tarea: ")
    nueva_tarea = {
        "id": proximo_id,
        "texto": texto,
        "completada": False
    }
    tareas.append(nueva_tarea)
    proximo_id += 1
    print("Tarea agregada.")
def marcar_completada():
    try:
        id_busqueda = int(input("Ingresa el ID de la tarea completada: "))
        for tarea in tareas:
            if tarea["id"] == id_busqueda:
                tarea["completada"] = True
                print("Tarea marcada como completada.")
                return
        print("ID no encontrado.")
    except ValueError:
        print("ID inválido.")
def eliminar_tarea():
    try:
        id_busqueda = int(input("Ingresa el ID de la tarea a eliminar: "))
        for tarea in tareas:
            if tarea["id"] == id_busqueda:
                tareas.remove(tarea)
                print("Tarea eliminada.")
                return
        print("ID no encontrado.")
    except ValueError:
        print("ID inválido.")
# ============================
#  Programa principal
# ============================
cargar_tareas()
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        ver_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "0":
        guardar_tareas()
        print("Tareas guardadas. ¡Hasta luego!")
        break
    else:
        print("Opción inválida.")