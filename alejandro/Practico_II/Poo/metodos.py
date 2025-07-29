class Estudiante:
  def __init__(self, nombre, edad, carrera):
      self.nombre = nombre
      self.edad = edad
      self.carrera = carrera
      self.materias = []
  # Método para presentarse
  def presentarse(self):
      print(f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}.")
  # Método para inscribirse en materias
  def inscribir_materia(self, nombre_materia):
      self.materias.append(nombre_materia)
      print(f"¡{self.nombre} se ha inscrito exitosamente en {nombre_materia}!")
# Ejemplo de uso
estudiante1 = Estudiante("Alejandro Romero", 21, "Ing. en Redes y Telecomunicaciones")
estudiante1.presentarse()
estudiante1.inscribir_materia("Programación II")
estudiante1.inscribir_materia("Taller de Sistemas Operativos I")
print(f"Materias de Alejandro: {estudiante1.materias}")
print ("Fin del programa ----- Richard hurtado")