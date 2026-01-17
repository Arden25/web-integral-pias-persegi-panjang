import streamlit as st
import numpy as np

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
  "Jumlah pias (n)",
  min_value=1,
  value=10,
  step=1
)

st.subheader("Lebar Pias")

if n > 0:
  h = (b - a) / n
  st.write("Nilai lebar pias (h):", h)

st.subheader("Hasil Integral (Metode Pias Persegi Panjang)")

if st.button("Hitung Integral"):
  try:
    h = (b - a) / n
    x = np.linspace(a, b - h, int(n))
    y = eval(fungsi)

    integral = np.sum(y * h)

    st.success(f"Hasil pendekatan integral = {integral}")

  except Exception:
    st.error("Terjadi kesalahan pada fungsi. Pastikan f(x) ditulis dengan benar.")
