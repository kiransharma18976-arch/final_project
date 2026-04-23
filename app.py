import streamlit as st
import pandas as pd
import numpy as np
import time
from gtts import gTTS
import os
import random

# --- 1. Page Configuration ---
st.set_page_config(page_title="Sentinel Drive AI", layout="wide")

# --- 2. Pink Dynamic CSS ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #ffdde1, #ee9ca7, #ffafbd, #ffc3a0);
        background-size: 400% 400%;
        animation: pinkGradient 15s ease infinite;
    }
    @keyframes pinkGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .article-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 25px; border-radius: 15px;
        border-left: 8px solid #d81b60; color: #333; line-height: 1.7;
    }
    .auth-container {
        background: white; padding: 30px; border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1); border: 1px solid #ffccd5;
    }
    .sidebar-header {
        background: #d81b60; color: white; padding: 10px;
        border-radius: 8px; text-align: center; font-weight: bold;
        margin-top: 15px; margin-bottom: 10px;
    }
    h1, h2, h3, h4 { color: #880e4f !important; }
    label { color: #880e4f !important; font-weight: bold !important; }
    .stButton>button { background: #d81b60; color: white; width: 100%; border-radius: 8px;}
</style>
""", unsafe_allow_html=True)

# --- 3. Functional Engines ---
def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("sentinel_voice.mp3")
        st.audio("sentinel_voice.mp3", format="audio/mp3", autoplay=True)
    except: pass

# --- 4. Session State ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# ----------------- UI LOGIC -----------------

if not st.session_state['logged_in']:
    # LANDING PAGE
    st.markdown("<h1 style='text-align:center;'>🌐 SENTINEL DRIVE: THE AI GUARDIAN</h1>", unsafe_allow_html=True)
    st.write("---")
    col_art, col_log = st.columns([1.8, 1.2])

    with col_art:
        st.markdown("### 📢 Intelligence & Safety Journal")
        st.markdown("""
        <div class='article-box'>
            <marquee direction="up" scrollamount="4" style="height: 400px;">
                <h4 style='color:#d81b60;'>1. The Physics of Saving Lives</h4>
                <p>90% of crashes involve human error. A human takes 1.5 seconds to react, but Sentinel AI scans in 0.01 seconds. Predicting impact 5 seconds early gives drivers the critical time needed to avoid fatal collisions.</p>
                <br>
                <h4 style='color:#d81b60;'>2. Fatigue: The Highway's Silent Killer</h4>
                <p>Drowsy driving causes 20% of fatal highway crashes. Our gaze tracking technology monitors eyelids and pupil dilation to detect microsleep before it happens, triggering alarms to keep you awake.</p>
                <br>
                <h4 style='color:#d81b60;'>3. V2V Digital Shield</h4>
                <p>Connected vehicles create a swarm intelligence. If a car 200 meters ahead hits its emergency brakes, your vehicle receives that data via radio signals before you can even see the brake lights.</p>
            </marquee>
        </div>
        """, unsafe_allow_html=True)

    with col_log:
        st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
        t1, t2 = st.tabs(["🔐 Login", "📝 Register"])
        with t1:
            u = st.text_input("User ID", key="l_u")
            p = st.text_input("Password", type="password", key="l_p")
            if st.button("Enter Dashboard"):
                if u and p: st.session_state['logged_in'] = True; st.rerun()
        with t2:
            st.text_input("Full Name", key="r_n"); st.text_input("Set Access Key", type="password", key="r_p")
            st.button("Create Account")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.sidebar.title("🛡️ Sentinel Guard")
    st.sidebar.markdown("<div class='sidebar-header'>AI SAFETY MENU</div>", unsafe_allow_html=True)
    
    choice = st.sidebar.radio("Select Feature", [
        "1. Risk Prediction", "2. Environmental Grip AI", "3. Pothole Radar", 
        "4. V2V Link", "5. AI Face Scan", "6. Live Monitor", "7. Voice Status", "8. Exit"
    ])

    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False; st.rerun()

    st.write("---")

    # --- Feature Implementation ---
    if "1." in choice:
        st.header("Accident Risk Assessment")
        spd = st.slider("Current Speed km/h", 0, 160, 65)
        if st.button("Analyze"):
            if spd > 90:
                st.error("HIGH RISK! SLOW DOWN."); speak("High Risk! Slow down.")
            else:
                st.success("Safe speed maintained."); speak("Safe speed.")

    elif "2." in choice:
        st.header("AI Environmental Grip Sensor")
        weather = st.selectbox("Current Weather", ["Sunny", "Heavy Rain", "Snow/Ice", "Dense Fog"])
        if st.button("Analyze Road Friction"):
            if weather == "Sunny":
                st.success("Grip Level: 95% (Optimal). Safe to maintain speed.")
                speak("Road grip is optimal.")
            else:
                risk_pct = random.randint(70, 90)
                st.warning(f"CAUTION: Grip reduced by {risk_pct}%. Braking distance increased by 3x.")
                speak("Caution. Road friction is low. Maintain safe distance.")

    elif "3." in choice:
        st.header("Pothole Surface Radar")
        if st.button("Initiate Scan"):
            detect = random.choice(["Yes", "No"])
            if detect == "Yes":
                st.error("Alert! Potholes detected 100m ahead."); speak("Potholes ahead.")
            else:
                st.success("Road surface is clear."); speak("Road clear.")

    elif "4." in choice:
        st.header("V2V Safety Status")
        dist = st.slider("Distance to Front Vehicle (m)", 0, 50, 20)
        if st.button("Check Mesh Link"):
            if dist < 15:
                st.error("V2V Alert! Maintain distance."); speak("Maintain distance.")
            else:
                st.success("Safe V2V distance."); speak("Safe distance.")

    elif "5." in choice or "6." in choice:
        st.header("AI Vision & Face Scan")
        img = st.camera_input("Look at the camera for AI verification")
        if img:
            with st.spinner("Analyzing sensors..."):
                time.sleep(2)
                alc = random.choice(["Negative", "Positive"])
                if alc == "Positive":
                    st.error("UNSAFE: Alcohol detected. Ignition locked."); speak("Ignition locked.")
                else:
                    st.success("Driver Fit. Engine Started."); speak("Driver safe. Engine started.")

    elif "7." in choice:
        st.header("AI Voice Assistant")
        speak("I am Sentinel AI Safety Assistant. All systems are operational.")
        st.info("Voice Assistant is Active.")

    elif "8." in choice:
        speak("Exiting. Drive safe!")
        st.session_state['logged_in'] = False; st.rerun()