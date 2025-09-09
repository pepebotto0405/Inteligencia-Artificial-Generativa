import streamlit as st
import numpy as np
import math

st.set_page_config(layout="wide")

st.title("Generador y Solucionador de Ecuaciones Cuadráticas 🎲")
st.markdown("Resuelve ecuaciones de la forma: **ax² + bx + c = 0**")
st.markdown("---")

# --- Generación de Ecuación Aleatoria ---
def generar_ecuacion():
    # Generar coeficientes a, b, c aleatoriamente
    # Aseguramos que 'a' no sea 0 para que sea una ecuación cuadrática
    a = np.random.randint(-10, 10)
    while a == 0:
        a = np.random.randint(-10, 10)
    b = np.random.randint(-10, 10)
    c = np.random.randint(-10, 10)
    
    return a, b, c

# --- Función para resolver la ecuación paso a paso ---
def resolver_ecuacion(a, b, c):
    pasos = []
    
    pasos.append(f"La ecuación dada es: **{a}x² + {b}x + {c} = 0**")
    pasos.append("Utilizamos la fórmula cuadrática: **x = [-b ± √(b² - 4ac)] / 2a**")
    
    delta = (b**2) - 4*a*c
    pasos.append(f"Calculamos el discriminante (Δ): **Δ = b² - 4ac**")
    pasos.append(f"Δ = ({b})² - 4({a})({c})")
    pasos.append(f"Δ = {b**2} - ({4*a*c})")
    pasos.append(f"Δ = {delta}")
    
    if delta < 0:
        pasos.append(f"Dado que el discriminante (Δ = {delta}) es negativo, no hay soluciones reales.")
        x1 = x2 = None
    elif delta == 0:
        pasos.append(f"Dado que el discriminante (Δ = {delta}) es cero, hay una solución real única.")
        x1 = -b / (2*a)
        pasos.append(f"x = -b / 2a")
        pasos.append(f"x = (-{b}) / (2*{a})")
        pasos.append(f"x = {x1:.4f}")
        x2 = x1
    else:
        pasos.append(f"Dado que el discriminante (Δ = {delta}) es positivo, hay dos soluciones reales distintas.")
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        
        pasos.append(f"Calculamos x1: x1 = (-b + √Δ) / 2a")
        pasos.append(f"x1 = (-{b} + √{delta}) / (2*{a})")
        pasos.append(f"x1 = (-{b} + {math.sqrt(delta):.4f}) / {2*a}")
        pasos.append(f"x1 = {x1:.4f}")
        
        pasos.append(f"Calculamos x2: x2 = (-b - √Δ) / 2a")
        pasos.append(f"x2 = (-{b} - √{delta}) / (2*{a})")
        pasos.append(f"x2 = (-{b} - {math.sqrt(delta):.4f}) / {2*a}")
        pasos.append(f"x2 = {x2:.4f}")
        
    return pasos, x1, x2

# --- Inicializar o generar nueva ecuación ---
if 'a' not in st.session_state:
    st.session_state.a, st.session_state.b, st.session_state.c = generar_ecuacion()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Ecuación a resolver:")
    ecuacion_str = f"{st.session_state.a}x²"
    if st.session_state.b > 0:
        ecuacion_str += f" + {st.session_state.b}x"
    elif st.session_state.b < 0:
        ecuacion_str += f" - {-st.session_state.b}x"
    
    if st.session_state.c > 0:
        ecuacion_str += f" + {st.session_state.c}"
    elif st.session_state.c < 0:
        ecuacion_str += f" - {-st.session_state.c}"
    
    ecuacion_str += " = 0"
    
    st.markdown(f"## {ecuacion_str}")
    
    st.markdown("---")
    st.subheader("Ingresa tus respuestas (aproxima a 4 decimales):")
    user_x1 = st.text_input("Valor de x1 (si aplica)", key="user_x1")
    user_x2 = st.text_input("Valor de x2 (si aplica)", key="user_x2")

    if st.button("Verificar y Mostrar Solución"):
        solucion_pasos, x1_real, x2_real = resolver_ecuacion(st.session_state.a, st.session_state.b, st.session_state.c)
        
        with col2:
            st.subheader("Solución Paso a Paso:")
            for paso in solucion_pasos:
                st.write(paso)
            
            st.markdown("---")
            st.subheader("Verificación de tus respuestas:")
            
            if x1_real is None: # No hay soluciones reales
                if user_x1 or user_x2:
                    st.error("No hay soluciones reales para esta ecuación. Tus respuestas no son correctas.")
                else:
                    st.success("¡Correcto! No hay soluciones reales y no ingresaste ninguna.")
            else:
                try:
                    user_x1_float = float(user_x1) if user_x1 else None
                    user_x2_float = float(user_x2) if user_x2 else None
                    
                    tolerance = 0.0001 # Tolerancia para comparar floats
                    
                    respuestas_correctas = []
                    if x1_real is not None:
                        respuestas_correctas.append(round(x1_real, 4))
                    if x2_real is not None and x1_real != x2_real: # Si hay dos soluciones distintas
                        respuestas_correctas.append(round(x2_real, 4))
                    
                    user_respuestas = []
                    if user_x1_float is not None:
                        user_respuestas.append(round(user_x1_float, 4))
                    if user_x2_float is not None:
                        user_respuestas.append(round(user_x2_float, 4))
                    
                    
                    correct_count = 0
                    if x1_real is not None and user_x1_float is not None and abs(user_x1_float - x1_real) < tolerance:
                        correct_count += 1
                    if x2_real is not None and user_x2_float is not None and abs(user_x2_float - x2_real) < tolerance and (abs(user_x2_float - x1_real) >= tolerance or user_x1_float is None):
                         correct_count +=1
                    # Aceptamos las respuestas en cualquier orden si son las mismas
                    if x1_real is not None and x2_real is not None and x1_real != x2_real:
                        if (user_x1_float is not None and user_x2_float is not None and
                            ((abs(user_x1_float - x1_real) < tolerance and abs(user_x2_float - x2_real) < tolerance) or
