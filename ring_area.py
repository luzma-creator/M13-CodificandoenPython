import math

def calcular_area_anillo(r_interior, r_exterior):
    """Calcula el área de un anillo dado el radio interior y el radio exterior."""
    area_exterior = math.pi * (r_exterior ** 2)
    area_interior = math.pi * (r_interior ** 2)
    area_anillo = area_exterior - area_interior
    return area_anillo

# Ejemplo de uso
r_interior = float(input("Ingresa el radio interior del anillo: "))
r_exterior = float(input("Ingresa el radio exterior del anillo: "))
area = calcular_area_anillo(r_interior, r_exterior)
print(f"El área del anillo con radio interior {r_interior} y radio exterior {r_exterior} es: {area}")