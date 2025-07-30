class CarritoDeCompras:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        # producto es un diccionario con "nombre" y "precio"
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for p in self.productos:
            total += p["precio"]
        return total

    def mostrar_carrito(self):
        print("Productos en el carrito:")
        for p in self.productos:
            print(f"- {p['nombre']} : ${p['precio']}")
        print(f"Total a pagar: ${self.calcular_total():.2f}")

# Ejemplo de uso
carrito = CarritoDeCompras()
carrito.agregar_producto({"nombre": "Camisa", "precio": 20})
carrito.agregar_producto({"nombre": "Pantalón", "precio": 35})
carrito.mostrar_carrito()