import streamlit as st
import pandas as pd
import numpy as np
import time
from gtts import gTTS
import os
import random
from datetime import datetime

# --- 1. Page Configuration ---
st.set_page_config(page_title="Sentinel Drive AI - Dark Edition", layout="wide")

# --- 2. High-Contrast Dark & Neon CSS ---
st.markdown("""
<style>
    /* Main Background - Deep Dark Blue */
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
        background-image: linear-gradient(180deg, #0e1117 0%, #07090d 100%);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }

    /* Professional Article Box */
    .article-box { 
        background: #1c2128; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #30363d; 
        color: #adbac7; 
        line-height: 1.6;
    }

    /* ALL TEXT Visibility - White/Cyan for contrast */
    h1, h2, h3, h4, label, p, span { 
        color: #58a6ff !important; 
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Metrics Styling */
    .stMetric { 
        background: #161b22; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #30363d;
    }
    [data-testid="stMetricValue"] { color: #39d353 !important; font-weight: bold; }

    /* Button Styling - Neon Blue */
    .stButton>button { 
        background-color: #238636; 
        color: white !important; 
        border-radius: 8px; 
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { 
        background-color: #2ea043;
        box-shadow: 0 0 15px #2ea043;
    }

    /* Auth Card Visibility */
    .auth-card { 
        background: #161b22; 
        padding: 40px; 
        border-radius: 15px; 
        border: 1px solid #30363d;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Tabs Visibility */
    .stTabs [data-baseweb="tab-list"] { background-color: transparent; }
    .stTabs [data-baseweb="tab"] { color: #8b949e !important; }
    .stTabs [aria-selected="true"] { color: #58a6ff !important; border-bottom-color: #58a6ff !important; }
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
if 'users_db' not in st.session_state: st.session_state['users_db'] = {"admin": "1234"}

# ----------------- UI LOGIC -----------------

if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align:center;'>🌌 SENTINEL DRIVE AI: THE SOVEREIGN</h1>", unsafe_allow_html=True)
    st.write("---")
    col_art, col_log = st.columns([1.6, 1.4])

    with col_art:
        st.markdown("### 📢 Intelligence & Safety Journal")
        st.markdown("""<div class='article-box'><marquee direction="up" scrollamount="2" style="height: 380px;">
        <h4 style='color:#58a6ff;'>🔥 Thermal Night Vision 2.0</h4><p>Pedestrian detection active up to 300m.</p><br>
        <h4 style='color:#58a6ff;'>🧠 Neural Fatigue Tracking</h4><p>Microsleep prevention sensors online.</p><br>
        <h4 style='color:#58a6ff;'>🛰️ Global SOS Network</h4><p>Satellite mesh connectivity established.</p><br>
        <h4 style='color:#58a6ff;'>🆕 Multi-User Access</h4><p>Create your safety profile in the register tab.</p>
        </marquee></div>""", unsafe_allow_html=True)

    with col_log:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])
        
        with tab1:
            u_login = st.text_input("Username", key="login_u")
            p_login = st.text_input("Password", type="password", key="login_p")
            if st.button("Unlock Dashboard"):
                if u_login in st.session_state['users_db'] and st.session_state['users_db'][u_login] == p_login:
                    speak(f"Access granted. Welcome {u_login}.")
                    st.session_state['logged_in'] = True; st.rerun()
                else: st.error("Invalid Access Key")
        
        with tab2:
            u_reg = st.text_input("New Username", key="reg_u")
            p_reg = st.text_input("New Password", type="password", key="reg_p")
            if st.button("Initialize Account"):
                if u_reg and p_reg:
                    st.session_state['users_db'][u_reg] = p_reg
                    st.success("Registration Successful!"); speak("Account created.")
                else: st.warning("Fields cannot be empty.")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- SIDEBAR ---
    st.sidebar.markdown("## 🛠️ CONTROL UNIT")
    choice = st.sidebar.selectbox("Select System", [
        "1. Live Telemetry", "2. Risk Prediction", "3. Environment & Grip", 
        "4. Pothole Radar", "5. V2V Digital Link", "6. AI Face Scan (Alcohol/Sleep)", 
        "7. Night Vision Mode", "8. Live Map Tracker", "9. Voice Status", "10. Black Box Logs"
    ])
    
    if st.sidebar.button("Shutdown System"):
        speak("Sentinel system off."); st.session_state['logged_in'] = False; st.rerun()

    st.markdown(f"## {choice}")

    # 1. LIVE TELEMETRY
    if "1." in choice:
        c1, c2, c3 = st.columns(3)
        c1.metric("AI Focus", "98%", "Optimal")
        c2.metric("Engine Temp", "42°C", "Stable")
        c3.metric("System Core", "88%", "Cool")
        st.line_chart(pd.DataFrame(np.random.randn(20, 1) + 65, columns=['Speed km/h']))
        if st.button("Diagnostic Report"): speak("All telemetry data within safe parameters.")

    # 2. RISK PREDICTION
    elif "2." in choice:
        spd = st.slider("Set Speed", 0, 200, 75)
        if st.button("Analyze Risk Profile"):
            if spd > 110:
                st.error("CRITICAL RISK!"); speak("Danger. Speed exceeds safe limits."); add_log("High Risk", f"Speed {spd}")
            else: st.success("Safe Operations."); speak("Speed is within safety range.")

    # 3. ENVIRONMENT
    elif "3." in choice:
        env = st.radio("Current Weather Data", ["Dry/Sunny", "Heavy Rain", "Snow/Ice"])
        if st.button("Analyze Grip"):
            speak(f"Weather scan complete. Road is {env}. Adjusting traction control."); add_log("Environment", env)

    # 4. POTHOLE RADAR
    elif "4." in choice:
        if st.button("Activate Ground Radar"):
            st.warning("Potholes ahead!"); speak("Warning. Surface irregularities detected ahead."); add_log("Hazard", "Pothole")

    # 5. V2V LINK
    elif "5." in choice:
        dist = st.number_input("Proximity to Lead Vehicle (m)", value=30)
        if st.button("Sync Mesh"):
            if dist < 12: st.error("Collision Alert!"); speak("Warning. Dangerous proximity.")
            else: st.success("Mesh Stable."); speak("Distance synchronized with swarm intelligence.")

    # 6. FACE SCAN
    elif "6." in choice:
        img = st.camera_input("Biometric Authentication")
        if img:
            status = random.choice(["Fit", "Drowsy", "Intoxicated"])
            if status == "Fit": st.success("Status: FIT"); speak("Driver state optimal. Enjoy your drive.")
            else: st.error(f"Status: {status}"); speak(f"Alert! Driver is {status}. System lock engaged."); add_log("Driver Condition", status)

    # 7. NIGHT VISION
    elif "7." in choice:
        st.image("https://wikimedia.org", caption="Active Thermal Tracking", use_container_width=True)
        if st.button("Thermal Scan"): speak("Infrared scanners active. Path is clear.")

    # 8. LIVE MAP
    elif "8." in choice:
        st.write("Tracking Swarm Location Data...")
        df_map = pd.DataFrame({'lat': [28.61, 28.62, 28.615], 'lon': [77.20, 77.21, 77.205]})
        st.map(df_map)
        if st.button("Sync Map"): speak("Navigation database updated. Avoiding congested risk zones.")

    # 9. VOICE STATUS
    elif "9." in choice:
        if st.button("System Health Check"): speak("All primary and secondary systems are functional. Global positioning active.")

    # 10. BLACK BOX
    elif "10." in choice:
        if st.session_state.logs: st.table(pd.DataFrame(st.session_state.logs))
        else: st.info("No safety incidents logged."); speak("Black box memory is clear.")

    st.write("---")
    st.caption("Sentinel Drive AI - Sovereign Pro Edition | Dark Mode Enabled")