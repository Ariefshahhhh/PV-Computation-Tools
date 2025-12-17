import streamlit as st

st.title("🌡 Temperature Coefficients")

alpha = st.number_input("α (Isc, %/°C)", value=0.045, format="%.3f")
beta  = st.number_input("β (Voc, %/°C)", value=-0.280, format="%.3f")
gamma = st.number_input("γ (Pmax, %/°C)", value=-0.350, format="%.3f")

T = st.session_state["Tmod"]

Ftemp_I = 1 + (alpha/100)*(T-25)
Ftemp_V = 1 + (beta/100)*(T-25)
Ftemp_P = 1 + (gamma/100)*(T-25)

st.session_state.update({
    "alpha": alpha,
    "beta": beta,
    "gamma": gamma,
    "Ftemp_I": Ftemp_I,
    "Ftemp_V": Ftemp_V,
    "Ftemp_P": Ftemp_P
})

if st.button("Next"):
    st.switch_page("pages/4_Loss_Factors.py")
