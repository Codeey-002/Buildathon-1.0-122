import streamlit as st
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=800, key="auto")

st.title("ECHO UI")


cols = st.columns(3)
buttons = [
    "YES","NO","HELP",
    "WATER","FOOD","MEDICINE",
    "CALL NURSE","PAIN","EMERGENCY"
]

for i, b in enumerate(buttons):
    cols[i%3].button(b)