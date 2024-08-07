def move_twice(x, y, direccion):
    """Mueve un punto (x, y) dos unidades en la dirección dada.

    Las direcciones posibles son 'arriba', 'abajo', 'izquierda', 'derecha'.
    """
    if direccion == 'arriba':
        y += 2
    elif direccion == 'abajo':
        y -= 2
    elif direccion == 'izquierda':
        x -= 2
    elif direccion == 'derecha':
        x += 2
    else:
        print("Dirección no válida. Usa 'arriba', 'abajo', 'izquierda' o 'derecha'.")
        return x, y

    return x, y


# Ejemplo de uso
x = float(input("Ingresa la coordenada x del punto inicial: "))
y = float(input("Ingresa la coordenada y del punto inicial: "))
direccion = input("Ingresa la dirección (arriba, abajo, izquierda, derecha): ").lower()
nuevo_x, nuevo_y = move_twice(x, y, direccion)
print(f"El nuevo punto después de mover dos unidades {direccion} es: ({nuevo_x}, {nuevo_y})")