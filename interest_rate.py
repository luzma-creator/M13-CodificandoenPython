def calcular_interes_simple(principal, tasa, tiempo):
    """Calcula el interés simple."""
    interes = principal * tasa * tiempo
    return interes

# Ejemplo de uso
principal = float(input("Ingresa el capital principal: "))
tasa = float(input("Ingresa la tasa de interés (en decimal): "))
tiempo = float(input("Ingresa el tiempo (en años): "))
interes = calcular_interes_simple(principal, tasa, tiempo)
print(f"El interés simple es: {interes}")