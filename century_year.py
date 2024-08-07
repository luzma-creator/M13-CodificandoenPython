def calcular_siglo(año):
    """Determina a qué siglo pertenece un año dado."""
    if año % 100 == 0:
        siglo = año // 100
    else:
        siglo = (año // 100) + 1
    return siglo

# Ejemplo de uso
año = int(input("Ingresa el año: "))
siglo = calcular_siglo(año)
print(f"El año {año} pertenece al siglo {siglo}.")