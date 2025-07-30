class CarritoDeCompras:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        if "nombre" in producto and "precio" in producto:
            self.productos.append(producto)
        else:
            print("Error: El producto debe tener 'nombre' y 'precio'.")

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto["precio"]
        return total

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(f"- {producto['nombre']} : ${producto['precio']}")
            print(f"Total: ${self.calcular_total()}")