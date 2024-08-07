import math

def calcular_volumen_esfera(radio):
    """Calcula el volumen de una esfera dado su radio."""
    volumen = (4/3) * math.pi * (radio ** 3)
    return volumen

# Ejemplo de uso
radio = float(input("Ingresa el radio de la esfera: "))
volumen = calcular_volumen_esfera(radio)
print(f"El volumen de la esfera con radio {radio} es: {volumen}")