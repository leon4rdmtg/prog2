import json
# -------- PARTE 1: GUARDAR EL INVENTARIO EN JSON --------
# Lista del inventario original
inventario = [
    {"producto": "Manzanas", "precio": 0.5, "stock": 100},
    {"producto": "Bananas", "precio": 0.3, "stock": 80},
    {"producto": "Naranjas", "precio": 0.6, "stock": 60}
]
# Guardar en archivo JSON (modo escritura)
nombre_archivo_json = "inventario.json"
with open(nombre_archivo_json, mode='w') as archivo_json:
    json.dump(inventario, archivo_json, indent=4)
print(" Inventario guardado exitosamente en 'inventario.json'.")
# -------- PARTE 2: CARGAR EL INVENTARIO DESDE JSON --------
# Leer el archivo JSON
with open(nombre_archivo_json, mode='r') as archivo_json:
    inventario_cargado_json = json.load(archivo_json)
# Mostrar el contenido cargado
print("\n Inventario cargado desde JSON:")
for item in inventario_cargado_json:
    print(item)
# Verificar tipo de dato de 'stock' del primer producto
print("\n Tipo de dato de 'stock':", type(inventario_cargado_json[0]['stock']))
print("\n--- Fin del programa ---- Jose Alejandro Zabala Romero")