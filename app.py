import streamlit as st
st.title("Mi aplicacion")
st.sidebar.header("Esta aplicacion es solo un demo")
st.sidebar.image("http://fcq.uach.mx/images/institucionales/Escudos/Dorado.png")
boton = st.button("globos")
if boton:
  st.balloon()
