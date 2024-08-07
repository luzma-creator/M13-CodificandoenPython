import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    area = math.pi * (radio ** 2)
    return area

# Ejemplo de uso
radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area}")