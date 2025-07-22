producto = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El Ceibo Ltda."
}
print(f"Producto: {producto['nombre']}")
print(f"Precio unitario: Bs {producto['precio_unitario']}")
producto["stock"] -= 5
producto["en_oferta"] = True
print("\nDatos actualizados del producto:")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")
print("\nFin del programa ----- jose alejandro zabala romero")