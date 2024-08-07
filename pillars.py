import matplotlib.pyplot as plt


def dibujar_pilares(alturas):
    """Dibuja una gráfica de pilares con alturas dadas."""
    x = list(range(len(alturas)))
    plt.bar(x, alturas, color='skyblue')

    plt.xlabel('Pilar')
    plt.ylabel('Altura')
    plt.title('Visualización de Pilares')
    plt.xticks(x, [f'Pilar {i + 1}' for i in x])

    plt.show()


# Ejemplo de uso
num_pilares = int(input("¿Cuántos pilares deseas dibujar? "))
alturas = []

for i in range(num_pilares):
    altura = float(input(f"Ingresa la altura del pilar {i + 1}: "))
    alturas.append(altura)

dibujar_pilares(alturas)