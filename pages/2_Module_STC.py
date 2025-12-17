import streamlit as st

st.title("📦 Module Electrical Data at STC")

Pstc = st.number_input("Pmax STC (W)", value=600.0)
Vmp = st.number_input("Vmp STC (V)", value=41.5)
Imp = st.number_input("Imp STC (A)", value=14.5)
Voc = st.number_input("Voc STC (V)", value=49.5)
Isc = st.number_input("Isc STC (A)", value=15.2)

st.session_state.update({
    "Pstc": Pstc,
    "Vmp_stc": Vmp,
    "Imp_stc": Imp,
    "Voc_stc": Voc,
    "Isc_stc": Isc
})

if st.button("Next"):
    st.switch_page("pages/3_Temperature.py")
