def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    area = (base * altura) / 2
    return area

# Ejemplo de uso
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area = calcular_area_triangulo(base, altura)
print(f"El área del triángulo con base {base} y altura {altura} es: {area}")

