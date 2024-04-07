import streamlit as st

edad = st.slider("Dime tu edad",max_value=130)

if edad<16:
  st.write("Es obligatorio que asistas a clase.")
else:
  if edad<67:
    st.write("Estás en edad de trabajar")
  else:
    st.write("A disfrutar de la jubilación")
