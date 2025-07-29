import json

# Datos en formato Python (lista de diccionarios)
datos_python = [{"nombre": "richard", "edad": 20}]

# Escritura del archivo JSON (serialización)
with open("datos.json", "w", encoding="utf-8") as archivo_json:
    json.dump(datos_python, archivo_json, indent=4, ensure_ascii=False)

# Lectura del archivo JSON (deserialización)
with open("datos.json", "r", encoding="utf-8") as archivo_json:
    datos_cargados = json.load(archivo_json)

# Verificación de tipos
print(type(datos_cargados))               # <class 'list'>
print(type(datos_cargados[0]['edad']))    # <class 'int'>
print(datos_cargados)                     # Muestra el contenido cargado
print ("fin del programa --- leonardo montenegro")