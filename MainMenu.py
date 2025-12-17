import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.title("⚡ Bifacial PV Computation Tool")
st.markdown("""
This wizard will guide you step-by-step to compute:

• Pmax  
• Vmp  
• Imp  
• Voc  
• Isc  

Click **Next** to begin.
""")

if st.button("Start"):
    st.switch_page("pages/1_Environmental.py")
