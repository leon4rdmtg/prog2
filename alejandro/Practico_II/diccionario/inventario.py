inventario = []
producto1 = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El Ceibo Ltda."
}
producto2 = {
    "codigo": "P002",
    "nombre": "Café de los Yungas",
    "precio_unitario": 40.00,
    "stock": 100,
    "proveedor": "Cafés Andinos"
}
producto3 = {
    "codigo": "P003",
    "nombre": "Quinua Real en Grano",
    "precio_unitario": 20.75,
    "stock": 80,
    "proveedor": "Granos Andinos"
}
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)
print("--- Inventario Actual ---")
print(f"Cantidad de productos diferentes: {len(inventario)}")
for producto in inventario:
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")
print("\nFin del programa ----- jose alejandro zabala romero")