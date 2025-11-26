import streamlit as st
import os
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=800, key="refresh")

st.title("ECHO UI Test")

cmd = ""
if os.path.exists("command.txt"):
    cmd = open("command.txt").read().strip()

st.write("Command received:", cmd)

cols = st.columns(3)
options = ["YES","NO","HELP",
           "WATER","FOOD","MEDICINE",
           "CALL NURSE","PAIN","EMERGENCY"]

for i, x in enumerate(options):
    cols[i % 3].button(x)