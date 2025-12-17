import streamlit as st

st.title("📊 Final Results & Calculation Steps")

s = st.session_state

Isc = s["Isc_stc"] * s["Ftemp_I"] * s["Fg"] * s["Fclean"] * s["Funshade"]
Voc = s["Voc_stc"] * s["Ftemp_V"]
Vmp = s["Vmp_stc"] * s["Ftemp_V"]
Imp = s["Imp_stc"] * s["Ftemp_I"] * s["Fg"] * s["Fclean"] * s["Funshade"]
Pmax = s["Pstc"] * s["Ftemp_P"] * s["Fg"] * s["Fclean"] * s["Funshade"] * s["Fmm"] * s["Fage"]

st.success(f"Maximum Power (Pmax) = {Pmax:.2f} W")
st.success(f"Voltage at MPP (Vmp) = {Vmp:.2f} V")
st.success(f"Current at MPP (Imp) = {Imp:.2f} A")
st.success(f"Open Circuit Voltage (Voc) = {Voc:.2f} V")
st.success(f"Short Circuit Current (Isc) = {Isc:.2f} A")

st.markdown("### 🧮 Calculation Steps")
st.write(f"Isc = {s['Isc_stc']} × {s['Ftemp_I']:.3f} × {s['Fg']} × {s['Fclean']} × {s['Funshade']}")
st.write(f"Voc = {s['Voc_stc']} × {s['Ftemp_V']:.3f}")
st.write(f"Vmp = {s['Vmp_stc']} × {s['Ftemp_V']:.3f}")
st.write(f"Imp = {s['Imp_stc']} × {s['Ftemp_I']:.3f} × {s['Fg']} × {s['Fclean']} × {s['Funshade']}")
st.write(f"Pmax = {s['Pstc']} × {s['Ftemp_P']:.3f} × {s['Fg']} × {s['Fclean']} × {s['Funshade']} × {s['Fmm']} × {s['Fage']}")
