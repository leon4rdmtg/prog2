class Libro:
    def __init__(self, titulo, autor, isbn, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.disponible = True
    def mostrar_info(self):
        print("=" * 50)
        print("INFORMACIÓN DEL LIBRO")
        print("=" * 50)
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print("=" * 50)
    def prestar_libro(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")
    def devolver_libro(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")
# Crear objetos
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-3-14-046401-7", 120)
libro2 = Libro("Raza de Bronce", "Alcides Arguedas", "978-99905-2-213-9", 250)
# Acceso directo a atributos
print(f"\nEl autor del primer libro es: {libro1.autor}")
print(f"El ISBN del segundo libro es: {libro2.isbn}")
# Mostrar info
print("\n--- Mostrando información completa ---")
libro1.mostrar_info()
libro2.mostrar_info()
# Probar métodos de comportamiento
print("\n--- Probando métodos de comportamiento ---")
libro1.prestar_libro()
libro1.prestar_libro()
libro1.devolver_libro()
libro1.devolver_libro()
print("\n--- Probando con libro2 ---")
libro2.prestar_libro()
libro2.devolver_libro()
print("\n--- Estado final de los libros ---")
libro1.mostrar_info()
libro2.mostrar_info()
print ("Fin del programa ----- Lucas Mateo Diaz Badan")