def calcular_igic(precio_base, porcentaje_igic):
    """Calcula el IGIC y el precio total dado el precio base y el porcentaje de IGIC."""
    igic = precio_base * (porcentaje_igic / 100)
    precio_total = precio_base + igic
    return igic, precio_total

# Ejemplo de uso
precio_base = float(input("Ingresa el precio base: "))
porcentaje_igic = float(input("Ingresa el porcentaje de IGIC: "))
igic, precio_total = calcular_igic(precio_base, porcentaje_igic)
print(f"El IGIC sobre un precio base de {precio_base} con un porcentaje del {porcentaje_igic}% es: {igic}")
print(f"El precio total con IGIC incluido es: {precio_total}")