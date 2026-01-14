import streamlit as st

st.title("Aplikasi Solusi Integral")
st.title("Metode Pias Persegi Panjang")

fungsi = st.text_input("Masukan fungsi f(x)", "x**2")

st.subheader("Batas Integral")

a = st.number_input(
  "Batas bawah (a)",
  value = 1.0,
  step = 0.1
)

b = st.number_input(
  "Batas atas (b)",
  value = 1.0,
  step = 0.1
)

st.subheader("Jumlah Pias")

n = st.number_input(
  "Jumlah pias (n)"
  min_value=1,
  value=10,
  step=1
)
