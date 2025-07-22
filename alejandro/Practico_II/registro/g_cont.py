# Lista principal que almacena todos los contactos
agenda_contactos = []
# Función para agregar un contacto nuevo
def agregar_contacto(contacto):
    agenda_contactos.append(contacto)
    print(f" Contacto '{contacto['nombre']}' agregado.")
# Función para buscar contactos por nombre (parcial o completo)
def buscar_por_nombre(nombre):
    resultados = [c for c in agenda_contactos if nombre.lower() in c["nombre"].lower()]
    return resultados
# Función para editar un campo de un contacto existente
def editar_contacto(nombre_original, campo, nuevo_valor):
    for c in agenda_contactos:
        if c["nombre"].lower() == nombre_original.lower():
            c[campo] = nuevo_valor
            print(f"✏️ Contacto '{c['nombre']}' actualizado.")
            return
    print(" Contacto no encontrado.")
# Función para eliminar un contacto por nombre
def eliminar_contacto(nombre):
    global agenda_contactos
    agenda_contactos = [c for c in agenda_contactos if c["nombre"].lower() != nombre.lower()]
    print(f"🗑️ Contacto '{nombre}' eliminado (si existía).")
# Función para mostrar todos los contactos en pantalla
def mostrar_contactos():
    if not agenda_contactos:
        print("📭 Agenda vacía.")
    else:
        print("\n---  Contactos ---")
        for c in agenda_contactos:
            print(f" {c['nombre']}")
            print(f"    Teléfonos: {', '.join(c['telefonos'])}")
            print(f"    Email: {c['email']}")
            print(f"    Dirección: {c['direccion']}")
            print(f"    Notas: {c['notas']}\n")
# ====================== SIMULACIÓN DE USO ======================
# Crear algunos contactos de ejemplo
contacto1 = {
    "nombre": "Alejandro Romero",
    "telefonos": ["78945612", "76543210"],
    "email": "alejandro@email.com",
    "direccion": "Av. cumavi",
    "notas": "Estudiante de informática"
}
contacto2 = {
    "nombre": "Lucía Fernández",
    "telefonos": ["76512345"],
    "email": "luciaf@gmail.com",
    "direccion": "Av cumavi",
    "notas": "Vecina"
}
# Agregar contactos
agregar_contacto(contacto1)
agregar_contacto(contacto2)
# Mostrar todos los contactos
mostrar_contactos()
# Buscar por nombre
print(" Buscando 'lucía':")
resultados = buscar_por_nombre("lucía")
for r in resultados:
    print(f" Encontrado: {r['nombre']} - {r['email']}")
# Editar un campo
editar_contacto("Lucía Fernández", "email", "lucia.fernandez@outlook.com")
# Mostrar los contactos actualizados
mostrar_contactos()
# Eliminar un contacto
eliminar_contacto("Alejandro Romero")
# Mostrar la agenda tras eliminar
mostrar_contactos()
print("Fin del programa ----- jose alejandro zabala romero")