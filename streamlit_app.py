import streamlit as st
from src.app import suma, saludo

st.title("Mi app con CI/CD")
st.write("Probando funciones desde src/app.py")

a = st.number_input("A", value=2)
b = st.number_input("B", value=3)
st.write("Suma:", suma(a, b))

nombre = st.text_input("Tu nombre", value="Sergio")
st.write(saludo(nombre))
