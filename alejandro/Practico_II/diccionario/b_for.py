producto = {'codigo': 'P001', 'nombre': 'Café', 'precio': 38.0, 'stock': 100}
print("\n--- Claves del producto ---")
for clave in producto:  # Itera sobre las claves por defecto
    print(clave)
print("\n--- Clave y Valor ---")
for clave in producto:
    valor = producto[clave]
    print(f"{clave.capitalize()}: {valor}")
#  métodos para más control:
print("\n--- Usando producto.keys() ---")
for clave in producto.keys():
    print(clave)
print("\n--- Usando producto.values() ---")
for valor in producto.values():
    print(valor)
print("\n--- Usando producto.items() ---")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")
# Uso de .get() para acceso seguro y evitar errores
descuento = producto.get('descuento', 0.0)  # 'descuento' no existe en el diccionario
print(f"\nDescuento aplicable: {descuento}")  # Imprime 0.0, el valor por defecto
print("\nFin del programa ----- jose alejandro zabala romero")