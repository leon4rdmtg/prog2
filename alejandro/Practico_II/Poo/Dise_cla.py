class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
    def esta_disponible(self):
        return self.stock > 0
    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock}")
class Cliente:
    def __init__(self, id, nombre, email, direccion_envio):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion_envio = direccion_envio
    def actualizar_direccion(self, nueva_direccion):
        self.direccion_envio = nueva_direccion
    def mostrar_info(self):
        print(f"Cliente: {self.nombre} | Email: {self.email} | Dirección: {self.direccion_envio}")
class CarritoDeCompras:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = {}  # clave: id del producto, valor: [producto, cantidad]
    def agregar_producto(self, producto, cantidad):
        if producto.id in self.productos:
            self.productos[producto.id][1] += cantidad
        else:
            self.productos[producto.id] = [producto, cantidad]
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos.values():
            total += producto.precio * cantidad
        return total
    def vaciar_carrito(self):
        self.productos.clear()
    def mostrar_carrito(self):
        print(f"\nCarrito de {self.cliente.nombre}:")
        for producto, cantidad in self.productos.values():
            print(f"- {producto.nombre}: {cantidad} unidades x ${producto.precio} = ${producto.precio * cantidad}")
        print(f"Total a pagar: ${self.calcular_total()}")
#  BLOQUE DE PRUEBA
if __name__ == "__main__":
    # Crear productos
    p1 = Producto(1, "Laptop", 1000, 5)
    p2 = Producto(2, "Mouse", 25, 20)
    p3 = Producto(3, "Auriculares", 50, 10)
    # Mostrar productos disponibles
    print("=== PRODUCTOS DISPONIBLES ===")
    p1.mostrar_info()
    p2.mostrar_info()
    p3.mostrar_info()
    # Crear cliente (Alejandro Romero)
    cliente1 = Cliente(1, "Alejandro Romero", "alejandro@example.com", "Av. Central 456")
    # Crear carrito para el cliente
    carrito = CarritoDeCompras(cliente1)
    # Agregar productos al carrito
    carrito.agregar_producto(p1, 1)  # 1 Laptop
    carrito.agregar_producto(p2, 2)  # 2 Mouse
    carrito.agregar_producto(p3, 1)  # 1 Auriculares
    # Mostrar el contenido del carrito
    carrito.mostrar_carrito()
print ("Fin del programa ----- Jose Alejandro Zabala Romero")