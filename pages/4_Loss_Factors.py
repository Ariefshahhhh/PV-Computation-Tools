import streamlit as st

st.title("⚙ Loss & Correction Factors")

Fg = st.number_input("Glass / Bifacial Gain Factor (Fg)", value=1.05, step=0.01)
Fclean = st.number_input("Cleaning Factor (Fclean)", value=0.98)
Funshade = st.number_input("Unshaded Factor (Funshade)", value=0.95)
Fmm = st.number_input("Mismatch Factor (Fmm)", value=0.98)
Fage = st.number_input("Aging Factor (Fage)", value=0.95)

st.session_state.update({
    "Fg": Fg,
    "Fclean": Fclean,
    "Funshade": Funshade,
    "Fmm": Fmm,
    "Fage": Fage
})

if st.button("Calculate Results"):
    st.switch_page("pages/5_Results.py")
