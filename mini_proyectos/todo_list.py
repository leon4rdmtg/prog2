import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
import os

tareas = []
archivo_tareas = "tareas.json"

def cargar_tareas():
    global tareas
    if os.path.exists(archivo_tareas):
        with open(archivo_tareas, "r", encoding="utf-8") as f:
            try:
                tareas = json.load(f)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "No se pudo cargar el archivo de tareas.")
                tareas = []
    else:
        tareas = []

def guardar_tareas():
    with open(archivo_tareas, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)

def actualizar_lista():
    tabla_tareas.delete(*tabla_tareas.get_children())
    for i, tarea in enumerate(tareas):
        estado = "✔ Completada" if tarea["completada"] else "❌ Pendiente"
        tabla_tareas.insert("", "end", iid=i, values=(tarea["texto"], tarea.get("fecha", "Sin fecha"), estado))

def agregar_tarea():
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Nueva tarea")

    tk.Label(ventana_emergente, text="Descripción:").pack(pady=5)
    entrada_texto = ttk.Entry(ventana_emergente, width=40)
    entrada_texto.pack(pady=5)

    tk.Label(ventana_emergente, text="Fecha límite:").pack(pady=5)
    selector_fecha = DateEntry(ventana_emergente, date_pattern='yyyy-mm-dd')
    selector_fecha.pack(pady=5)

    def guardar():
        texto = entrada_texto.get()
        fecha = selector_fecha.get()
        if texto:
            tareas.append({
                "texto": texto,
                "fecha": fecha,
                "completada": False
            })
            guardar_tareas()
            actualizar_lista()
            ventana_emergente.destroy()

    ttk.Button(ventana_emergente, text="Guardar tarea", command=guardar).pack(pady=10)

def completar_tarea():
    seleccion = tabla_tareas.focus()
    if seleccion:
        i = int(seleccion)
        tareas[i]["completada"] = True
        guardar_tareas()
        actualizar_lista()
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para completar.")

def eliminar_tarea():
    seleccion = tabla_tareas.focus()
    if seleccion:
        i = int(seleccion)
        tareas.pop(i)
        guardar_tareas()
        actualizar_lista()
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("TO-DO List con Columnas")

# Crear tabla de tareas
tabla_tareas = ttk.Treeview(ventana, columns=("Descripción", "Fecha", "Estado"), show="headings", height=10)
tabla_tareas.heading("Descripción", text="Descripción")
tabla_tareas.heading("Fecha", text="Fecha límite")
tabla_tareas.heading("Estado", text="Estado")

tabla_tareas.column("Descripción", width=200)
tabla_tareas.column("Fecha", width=100)
tabla_tareas.column("Estado", width=100)
tabla_tareas.pack(padx=10, pady=10)

# Crear botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

ttk.Button(frame_botones, text="Agregar tarea", command=agregar_tarea).grid(row=0, column=0, padx=5)
ttk.Button(frame_botones, text="Marcar como completada", command=completar_tarea).grid(row=0, column=1, padx=5)
ttk.Button(frame_botones, text="Eliminar tarea", command=eliminar_tarea).grid(row=0, column=2, padx=5)

# Cargar tareas guardadas
cargar_tareas()
actualizar_lista()

# Ejecutar ventana
ventana.mainloop()