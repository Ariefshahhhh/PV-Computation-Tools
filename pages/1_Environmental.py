import streamlit as st

st.title("🔆 Environmental Inputs")

G_front = st.number_input("Front Irradiance (W/m²)", value=800.0)
BG = st.number_input("Bifacial Gain BG (from datasheet)", value=0.10, format="%.3f")
Tmod = st.number_input("Module Temperature (°C)", value=30.0)

G_rear = BG * G_front
G_total = G_front + G_rear

st.info(f"Rear irradiance = {G_rear:.2f} W/m²")
st.info(f"Total irradiance = {G_total:.2f} W/m²")

st.session_state.update({
    "G_front": G_front,
    "BG": BG,
    "G_rear": G_rear,
    "G_total": G_total,
    "Tmod": Tmod
})

if st.button("Next"):
    st.switch_page("pages/2_Module_STC.py")
