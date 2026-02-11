import streamlit as st

st.set_page_config(page_title="Pago de Luz", page_icon=":bulb:", layout="centered")

st.title("Pronostico de Proximo Pago de Luz")
st.write("Calcula un estimado simple usando tu ultimo recibo y el consumo del mes.")

st.header("Datos de entrada")
consumo_mes = st.number_input("Consumo del mes (kWh)", min_value=0.0, value=300.0, step=10.0)
tarifa_kwh = st.number_input("Tarifa por kWh ($)", min_value=0.0, value=0.18, step=0.01, format="%.2f")
cargo_fijo = st.number_input("Cargo fijo ($)", min_value=0.0, value=5.0, step=1.0)

st.header("Ajustes opcionales")
aumento_pct = st.slider("Aumento esperado (%)", min_value=0, max_value=30, value=0, step=1)

st.divider()

subtotal = consumo_mes * tarifa_kwh
subtotal_ajustado = subtotal * (1 + aumento_pct / 100)

pago_estimado = subtotal_ajustado + cargo_fijo

st.subheader("Resultado")
st.write(f"Subtotal por consumo: **${subtotal:.2f}**")
st.write(f"Subtotal ajustado: **${subtotal_ajustado:.2f}**")
st.write(f"Pago estimado total: **${pago_estimado:.2f}**")

st.caption("Estimacion simple. No reemplaza el recibo oficial.")
