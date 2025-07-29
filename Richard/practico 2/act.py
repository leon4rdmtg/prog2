class CarritoDeCompras:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(p["precio"] for p in self.productos)

    def mostrar_carrito(self):
        for p in self.productos:
            print(f'Producto: {p["nombre"]} - Precio: {p["precio"]}')
        print(f"Total: {self.calcular_total()}")

carrito = CarritoDeCompras()

carrito.agregar_producto({"nombre": "papa", "precio": 5})
carrito.agregar_producto({"nombre": "tomate", "precio": 8})
carrito.agregar_producto({"nombre": "Huevos", "precio": 10})

carrito.mostrar_carrito()
