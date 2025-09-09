import streamlit as st
from datetime import datetime

# Título de la aplicación
st.title("🗓️ Agenda de Reuniones")
st.markdown("---")

# Datos de la agenda sin base de datos
# Puedes agregar, modificar o eliminar reuniones aquí
reuniones = [
    {"fecha": "2025-09-15", "hora": "10:00", "tema": "Revisión de proyecto A", "participantes": "Juan, María"},
    {"fecha": "2025-09-15", "hora": "15:30", "tema": "Planificación del trimestre", "participantes": "Equipo de desarrollo"},
    {"fecha": "2025-09-16", "hora": "09:00", "tema": "Presentación a clientes", "participantes": "Gerencia, Equipo comercial"},
    {"fecha": "2025-09-17", "hora": "11:00", "tema": "Sesión de brainstorming", "participantes": "Todo el equipo"}
]

# Conversión a formato de fecha para ordenar
for reunion in reuniones:
    reunion['datetime'] = datetime.strptime(f"{reunion['fecha']} {reunion['hora']}", "%Y-%m-%d %H:%M")

# Ordenar las reuniones por fecha y hora
reuniones_ordenadas = sorted(reuniones, key=lambda x: x['datetime'])

# Mostrar la agenda en una visualización de tabla
st.subheader("Próximas Reuniones")
for reunion in reuniones_ordenadas:
    st.info(
        f"**{reunion['fecha']} - {reunion['hora']}**\n\n"
        f"**Tema:** {reunion['tema']}\n\n"
        f"**Participantes:** {reunion['participantes']}"
    )
