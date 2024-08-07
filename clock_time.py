from datetime import datetime

def mostrar_hora_actual():
    """Muestra la hora actual en formato de reloj (hora, minutos, segundos)."""
    ahora = datetime.now()
    hora = ahora.strftime("%H:%M:%S")
    return hora

# Ejemplo de uso
hora_actual = mostrar_hora_actual()
print(f"La hora actual es: {hora_actual}")