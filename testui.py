import streamlit as st

st.title("ECHO UI Prototype")

options = [
    "YES", "NO", "HELP",
    "WATER", "FOOD", "MEDICINE",
    "CALL NURSE", "PAIN", "EMERGENCY"
]

cols = st.columns(3)

for i, opt in enumerate(options):
    cols[i % 3].button(opt, key=f"btn_{i}")