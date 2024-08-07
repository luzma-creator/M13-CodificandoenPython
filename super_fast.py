def suma_rapida(n):
    """Calcula la suma de los primeros n números naturales de manera eficiente."""
    return n * (n + 1) // 2

# Ejemplo de uso
n = int(input("Ingresa un número entero positivo: "))
suma = suma_rapida(n)
print(f"La suma de los primeros {n} números naturales es: {suma}")