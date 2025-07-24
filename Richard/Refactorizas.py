
def calcular_area_rectangulo(base, altura):
    return base * altura
   
def mostrar_area_rectangulo(numero, base, altura): 
    area = calcular_area_rectangulo(base, altura) 
    
    print(f"El área del rectángulo {numero} ({base}x{altura}) es: {area}") 

mostrar_area_rectangulo(1, 10, 5)

mostrar_area_rectangulo(2, 7, 3)

mostrar_area_rectangulo(3, 15, 8)
print("fin del programa richard hurtado")