import math

def calcular_distancia_euclidiana(x1, y1, x2, y2):
    """Calcula la distancia euclidiana entre dos puntos (x1, y1) y (x2, y2)."""
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

# Ejemplo de uso
x1 = float(input("Ingresa la coordenada x del primer punto: "))
y1 = float(input("Ingresa la coordenada y del primer punto: "))
x2 = float(input("Ingresa la coordenada x del segundo punto: "))
y2 = float(input("Ingresa la coordenada y del segundo punto: "))
distancia = calcular_distancia_euclidiana(x1, y1, x2, y2)
print(f"La distancia euclidiana entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia}")