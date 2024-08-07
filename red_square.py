def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el tamaño de su lado."""
    area = lado ** 2
    return area

def calcular_perimetro_cuadrado(lado):
    """Calcula el perímetro de un cuadrado dado el tamaño de su lado."""
    perimetro = 4 * lado
    return perimetro

# Ejemplo de uso
lado = float(input("Ingresa el tamaño del lado del cuadrado: "))
area = calcular_area_cuadrado(lado)
perimetro = calcular_perimetro_cuadrado(lado)
print(f"El área del cuadrado con lado {lado} es: {area}")
print(f"El perímetro del cuadrado con lado {lado} es: {perimetro}")