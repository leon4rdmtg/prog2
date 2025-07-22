def contar_elementos_buscados():
  lista_fija = (1, 2, 3, 4, 2, 6, 7, 8, 9, 10) 
  contador = 0

  print("Contador de elementos buscados en la lista:")
  print(f"Lista actual: {lista_fija}")

  for elemento in lista_fija:
      respuesta = input(f"¿Es '{elemento}' el elemento que buscas? (y/n): ")

      while respuesta not in ['y', 'n']:
          print("Respuesta no válida. Por favor ingresa 'y' o 'n'.")
          respuesta = input(f"¿Es '{elemento}' el elemento que buscas? (y/n): ")

      if respuesta == 'y':
          contador += 1

  print(f"\nTotal de elementos encontrados: {contador}")

contar_elementos_buscados()
