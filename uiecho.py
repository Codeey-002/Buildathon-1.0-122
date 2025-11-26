import streamlit as st
import os
from streamlit_autorefresh import st_autorefresh
import pyttsx3

tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 170)
tts_engine.setProperty("volume", 1.0)

def speak(text):
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except:
        pass

st_autorefresh(interval=500, key="ref")
st.set_page_config(page_title="ECHO UI", layout="centered")

options = [
    "YES", "NO", "HELP",
    "WATER", "FOOD", "MEDICINE",
    "CALL NURSE", "PAIN", "EMERGENCY"
]

if "cursor" not in st.session_state:
    st.session_state.cursor = 0

if "confirmed" not in st.session_state:
    st.session_state.confirmed = ""

cmd = ""
if os.path.exists("cmmd.txt"):
    with open("cmmd.txt", "r") as f:
        cmd = f.read().strip()

if cmd == "MOVE":
    st.session_state.cursor = (st.session_state.cursor + 1) % len(options)

elif cmd == "CONFIRM":
    selected = options[st.session_state.cursor]
    st.session_state.confirmed = selected
    st.toast(f"CONFIRMED: {selected}")
    speak(f"{selected} selected")  

if cmd:
    open("cmmd.txt", "w").close()


st.markdown(
    """
    <h1 style='text-align:center; font-size:42px; margin-bottom:0px;'>E C H O</h1>
    <p style='text-align:center; color:#BBBBBB; margin-top:-8px; font-size:18px;'>
        Eye-Blink Controlled Dashboard
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---")


st.markdown(
    """
    <div style="
        background-color:#2e2e2e;
        padding:15px;
        border-radius:10px;
        border:1px solid #444;
        margin-bottom:20px;
    ">
        <h4 style="color:#FFD700; margin:0; text-align:center;">
            👁️ How to Use Blink Controls
        </h4>
        <p style="color:#ddd; font-size:16px; text-align:center; margin-top:8px;">
            • <b>Single Blink</b> → Move the highlight to the next option <br>
            • <b>Double Blink</b> → Confirm the highlighted option <br>
            • Blink naturally (don't squeeze) and stay in camera frame.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="text-align:center; margin-bottom:10px;">
        <span style="font-size:22px; color:#DDD;">Current Highlight:</span><br>
        <span style="font-size:30px; color:#FFD700; font-weight:bold;">
            {options[st.session_state.cursor]}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

if st.session_state.confirmed:
    st.success(f"Last Confirmed: {st.session_state.confirmed}")

st.write("---")


cols = st.columns(3)
for i, opt in enumerate(options):
    col = cols[i % 3]

    if i == st.session_state.cursor:
        bg = "#FFD700"
        color = "black"
        border = "4px solid #FFEB55"
        shadow = "0px 0px 15px rgba(255, 215, 0, 0.6)"
    else:
        bg = "#222"
        color = "white"
        border = "2px solid #444"
        shadow = "0px 0px 8px rgba(0,0,0,0.4)"

    col.markdown(
        f"""
        <div style="
            background-color:{bg};
            color:{color};
            border:{border};
            padding:18px;
            margin:12px;
            border-radius:12px;
            text-align:center;
            font-size:20px;
            font-weight:600;
            box-shadow:{shadow};
            height:80px;
            display:flex;
            align-items:center;
            justify-content:center;
        ">
            {opt}
        </div>
        """,
        unsafe_allow_html=True
    )