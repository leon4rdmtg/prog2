        import tkinter as tk
        from tkinter import messagebox, simpledialog

        # Variables globales
        lista_de_tareas = []
        proximo_id_tarea = 1

        # Funciones principales
        def agregar_tarea():
            global proximo_id_tarea
            descripcion = entry_desc.get()
            prioridad = prioridad_var.get()

            if not descripcion.strip():
                messagebox.showwarning("Campo vacío", "Por favor escribe una descripción.")
                return

            nueva_tarea = {
                "id": proximo_id_tarea,
                "descripcion": descripcion,
                "completada": False,
                "prioridad": prioridad
            }
            lista_de_tareas.append(nueva_tarea)
            proximo_id_tarea += 1
            actualizar_lista()
            entry_desc.delete(0, tk.END)

        def buscar_tarea_por_id(id_buscado):
            for tarea in lista_de_tareas:
                if tarea["id"] == id_buscado:
                    return tarea
            return None

        def marcar_completada():
            try:
                seleccion = lista.curselection()
                if not seleccion:
                    messagebox.showwarning("Selecciona una tarea", "Debes seleccionar una tarea.")
                    return

                texto_tarea = lista.get(seleccion[0])
                id_tarea = int(texto_tarea.split("ID: ")[1].split(" |")[0])
                tarea = buscar_tarea_por_id(id_tarea)
                if tarea:
                    tarea["completada"] = True
                    actualizar_lista()
                else:
                    messagebox.showerror("Error", f"No se encontró la tarea con ID {id_tarea}.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        def eliminar_tarea():
            try:
                seleccion = lista.curselection()
                if not seleccion:
                    messagebox.showwarning("Selecciona una tarea", "Debes seleccionar una tarea.")
                    return

                texto_tarea = lista.get(seleccion[0])
                id_tarea = int(texto_tarea.split("ID: ")[1].split(" |")[0])
                tarea = buscar_tarea_por_id(id_tarea)
                if tarea:
                    lista_de_tareas.remove(tarea)
                    actualizar_lista()
                else:
                    messagebox.showerror("Error", f"No se encontró la tarea con ID {id_tarea}.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        def actualizar_lista():
            lista.delete(0, tk.END)
            for tarea in lista_de_tareas:
                estado = "✔" if tarea["completada"] else "⏳"
                texto = f"{estado} ID: {tarea['id']} | {tarea['descripcion']} (Prioridad: {tarea['prioridad']})"
                lista.insert(tk.END, texto)

        # Configuración de la ventana
        ventana = tk.Tk()
        ventana.title("📝 To-Do List con Tkinter")
        ventana.geometry("600x400")

        # Entrada para la descripción
        tk.Label(ventana, text="Descripción de la tarea:").pack()
        entry_desc = tk.Entry(ventana, width=60)
        entry_desc.pack(pady=5)

        # Opción de prioridad
        prioridad_var = tk.StringVar(value="media")
        tk.Label(ventana, text="Prioridad:").pack()
        prioridad_menu = tk.OptionMenu(ventana, prioridad_var, "alta", "media", "baja")
        prioridad_menu.pack()

        # Botones de acción
        frame_botones = tk.Frame(ventana)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Tarea", command=agregar_tarea).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea).grid(row=0, column=2, padx=5)

        # Lista de tareas
        lista = tk.Listbox(ventana, width=100)
        lista.pack(pady=10, expand=True)

        # Ejecutar la aplicación
        ventana.mainloop()
