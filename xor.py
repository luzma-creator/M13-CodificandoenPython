def realizar_xor(a, b):
    """Realiza la operación XOR bit a bit entre dos números enteros."""
    resultado = a ^ b
    return resultado

# Ejemplo de uso
a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))
resultado = realizar_xor(a, b)
print(f"El resultado de {a} XOR {b} es: {resultado}")