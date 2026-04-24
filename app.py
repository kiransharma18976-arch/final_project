import streamlit as st
import pandas as pd
import numpy as np
import time
from gtts import gTTS
import os
import random
from datetime import datetime

# --- 1. Page Configuration ---
st.set_page_config(page_title="Sentinel Drive AI - Sovereign Edition", layout="wide")

# --- 2. Advanced Pink & Glassmorphism CSS ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #ffdde1, #ee9ca7, #ffafbd, #ffc3a0);
        background-size: 400% 400%;
        animation: pinkGradient 15s ease infinite;
    }
    @keyframes pinkGradient { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    .article-box { background: rgba(255, 255, 255, 0.85); padding: 20px; border-radius: 15px; border-left: 8px solid #d81b60; }
    .stMetric { background: white; padding: 15px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    .stButton>button { background: #d81b60; color: white; border-radius: 10px; font-weight: bold; height: 3em; border: none; width: 100%;}
    .stButton>button:hover { background: #ad1457; transform: translateY(-2px); }
    .auth-card { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# --- 3. Core Functional Engines ---
def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("sentinel_voice.mp3")
        st.audio("sentinel_voice.mp3", format="audio/mp3", autoplay=True)
    except: pass

def add_log(event, status):
    if 'logs' not in st.session_state: st.session_state.logs = []
    st.session_state.logs.append({"Time": datetime.now().strftime("%H:%M:%S"), "Event": event, "Status": status})

# --- 4. Session State Init ---
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'logs' not in st.session_state: st.session_state['logs'] = []
if 'users_db' not in st.session_state: st.session_state['users_db'] = {"admin": "1234"} # Default user

# ----------------- UI LOGIC -----------------

if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align:center;'>🌐 SENTINEL DRIVE AI: THE SOVEREIGN</h1>", unsafe_allow_html=True)
    st.write("---")
    col_art, col_log = st.columns([1.6, 1.4])

    with col_art:
        st.markdown("### 📢 Intelligence & Safety Journal")
        st.markdown("""<div class='article-box'><marquee direction="up" scrollamount="3" style="height: 380px;">
        <h4 style='color:#d81b60;'>🔥 Thermal Night Vision 2.0</h4><p>Now detects pedestrians and animals 300 meters away in pitch black.</p><br>
        <h4 style='color:#d81b60;'>🧠 Neural Fatigue Tracking</h4><p>AI monitors brainwave patterns through eye-reflex to prevent microsleep.</p><br>
        <h4 style='color:#d81b60;'>🛰️ Global SOS Network</h4><p>Emergency beacon connects via Starlink if cellular network fails.</p><br>
        <h4 style='color:#d81b60;'>🆕 Multi-User Access</h4><p>New drivers can now register and create personal safety profiles.</p>
        </marquee></div>""", unsafe_allow_html=True)

    with col_log:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["🔑 Login", "📝 Register New User"])
        
        with tab1:
            u_login = st.text_input("Username", key="login_u")
            p_login = st.text_input("Password", type="password", key="login_p")
            if st.button("Unlock Dashboard"):
                if u_login in st.session_state['users_db'] and st.session_state['users_db'][u_login] == p_login:
                    speak(f"Welcome back {u_login}. System initialized.")
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Invalid Credentials")
        
        with tab2:
            u_reg = st.text_input("Create Username", key="reg_u")
            p_reg = st.text_input("Create Password", type="password", key="reg_p")
            if st.button("Create Account"):
                if u_reg and p_reg:
                    st.session_state['users_db'][u_reg] = p_reg
                    st.success("Account Created! You can now login.")
                    speak("Account successfully created.")
                else:
                    st.warning("Please fill all fields.")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- SIDEBAR NAVIGATION ---
    st.sidebar.markdown("### 🛠️ CONTROL PANEL")
    choice = st.sidebar.selectbox("Active Feature", [
        "1. Live Telemetry", "2. Risk Prediction", "3. Environment & Grip", 
        "4. Pothole Radar", "5. V2V Digital Link", "6. AI Face Scan (Alcohol/Sleep)", 
        "7. Night Vision Mode", "8. Live Map Tracker", "9. Voice Status", "10. Black Box Logs"
    ])
    
    if st.sidebar.button("System Shutdown"):
        speak("Sentinel shutting down. Drive safely.")
        st.session_state['logged_in'] = False; st.rerun()

    st.write(f"## {choice}")

    # 1. LIVE TELEMETRY
    if "1." in choice:
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Focus Score", "98%", "Stable")
        col_b.metric("Tire Temp", "42°C", "+2°")
        col_c.metric("Battery", "88%", "-1%")
        st.line_chart(pd.DataFrame(np.random.randn(15, 1) + 60, columns=['Speed']))
        if st.button("Analyze Stats"): speak("System health is optimal. Efficiency at 98 percent.")

    # 2. RISK PREDICTION
    elif "2." in choice:
        spd = st.slider("Vehicle Speed", 0, 200, 80)
        if st.button("Predict Accident Probability"):
            if spd > 110:
                st.error("HIGH DANGER: Collision probability is 75%"); speak("Danger! Reduce speed. High risk of collision.")
                add_log("High Risk", f"Speed {spd}")
            else:
                st.success("Safe Zone."); speak("You are in a safe speed zone.")

    # 3. ENVIRONMENT
    elif "3." in choice:
        env = st.radio("Current Weather", ["Dry", "Wet", "Icy"])
        if st.button("Calculate Grip"):
            res = "Grip 90%" if env == "Dry" else "Grip 40%"
            st.warning(res); speak(f"Warning. Road is {env}. Grip level reduced.")
            add_log("Weather Alert", env)

    # 4. POTHOLE RADAR
    elif "4." in choice:
        if st.button("Scan Road Geometry"):
            msg = "Potholes detected in 50 meters!"
            st.error(msg); speak(msg); add_log("Hazard", "Pothole")

    # 5. V2V LINK
    elif "5." in choice:
        dist = st.number_input("Front Car Distance (m)", value=25)
        if st.button("Sync V2V"):
            if dist < 10:
                st.error("Critical Proximity!"); speak("Warning. Too close to the front vehicle.")
            else:
                st.success("Synchronized."); speak("Distance synchronized with front vehicle.")

    # 6. FACE SCAN (ALCOHOL/SLEEP)
    elif "6." in choice:
        img = st.camera_input("AI Biometric Scan")
        if img:
            status = random.choice(["Fit", "Drowsy", "Intoxicated"])
            if status == "Fit":
                st.success("Driver Fit."); speak("Driver fit. Ignition unlocked.")
            else:
                st.error(f"Alert: Driver {status}"); speak(f"Warning! Driver is {status}. Emergency SOS initiated."); add_log("Driver Condition", status)

    # 7. NIGHT VISION
    elif "7." in choice:
        st.info("Thermal Contrast Mode Active")
        st.image("https://wikimedia.org", caption="Thermal Feed (Object Detection)", use_column_width=True)
        if st.button("Scan Dark Zones"): speak("Night vision active. Heat signature detected near lane 2.")

    # 8. LIVE MAP
    elif "8." in choice:
        st.write("Tracking Active Incident Zones...")
        # Random coordinates around Delhi for demo
        df_map = pd.DataFrame({'lat': [28.6139, 28.6210, 28.6100], 'lon': [77.2090, 77.2150, 77.2000]})
        st.map(df_map)
        if st.button("Update Map"): speak("Map updated. Two accident zones detected nearby. Re-routing recommended.")

    # 9. VOICE STATUS
    elif "9." in choice:
        if st.button("System Diagnostic"): speak("All sensors are active. Satellite link established. Oxygen levels normal. All systems go.")

    # 10. BLACK BOX
    elif "10." in choice:
        if st.session_state.logs:
            st.table(pd.DataFrame(st.session_state.logs))
        else: st.write("No logs."); speak("Black box data is empty.")

    st.write("---")
    st.caption("Sentinel Drive AI - Sovereign Pro Edition | Satellite Connectivity Enabled")