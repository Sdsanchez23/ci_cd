import streamlit as st
import math

st.set_page_config(page_title="Calculadora Solar", page_icon=":sunny:", layout="centered")

st.markdown(
    """
    <style>
      .stApp { background-color: #FFF7E6; }
      h1, h2, h3, h4, h5, h6 { color: #F57C00; }
      .stButton>button { background-color: #F57C00; color: white; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Calculadora Solar y Ahorro")
st.write("Estima produccion, ahorro y recuperacion de inversion para paneles solares.")

st.header("1) Datos de tu hogar")
consumo_mensual = st.number_input("Consumo mensual (kWh)", min_value=0.0, value=300.0, step=10.0)
tarifa_kwh = st.number_input("Tarifa electrica ($/kWh)", min_value=0.0, value=0.18, step=0.01, format="%.2f")

st.header("2) Datos solares")
sol_horas = st.number_input("Horas solares pico por dia (promedio)", min_value=0.0, value=5.0, step=0.5)
eficiencia = st.slider("Eficiencia del sistema (%)", min_value=60, max_value=95, value=80, step=1)

st.header("3) Sistema propuesto")
capacidad_kw = st.number_input("Tamano del sistema (kW)", min_value=0.0, value=3.0, step=0.5)
costo_sistema = st.number_input("Costo total del sistema ($)", min_value=0.0, value=6000.0, step=500.0)

st.divider()

# Calculos
produccion_diaria = capacidad_kw * sol_horas * (eficiencia / 100.0)
produccion_mensual = produccion_diaria * 30
produccion_anual = produccion_diaria * 365

ahorro_mensual = min(produccion_mensual, consumo_mensual) * tarifa_kwh
ahorro_anual = ahorro_mensual * 12

if ahorro_anual > 0:
    payback = costo_sistema / ahorro_anual
else:
    payback = math.inf

st.subheader("Resultados")
st.write(f"Produccion estimada mensual: **{produccion_mensual:.1f} kWh**")
st.write(f"Produccion estimada anual: **{produccion_anual:.0f} kWh**")
st.write(f"Ahorro estimado mensual: **${ahorro_mensual:.2f}**")
st.write(f"Ahorro estimado anual: **${ahorro_anual:.2f}**")

if math.isfinite(payback):
    st.write(f"Tiempo estimado de recuperacion: **{payback:.1f} anos**")
else:
    st.write("Tiempo estimado de recuperacion: **No calculable**")

st.caption("Resultados aproximados. No reemplaza un estudio tecnico real.")
