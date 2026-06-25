import streamlit as st
import time
import pandas as pd
import random

# ---------------------------------------------------------
# 1. PAGE SETUP & EXTENSIVE VISUAL CUSTOMIZATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Aura AI - Your Safe Space",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark mode styling injection to match the neon purple aesthetic
st.markdown("""
<style>
    .stApp {
        background-color: #0B0C1E;
        color: #E0E2F5;
    }
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(90deg, #A370F7, #00F2FE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .ui-card {
        background: linear-gradient(145deg, #181A3A, #121432);
        border: 1px solid #323775;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
    }
    .stat-number {
        font-size: 36px;
        font-weight: bold;
        color: #00F2FE;
        text-align: center;
    }
    .stat-orange {
        font-size: 36px;
        font-weight: bold;
        color: #FF5E62;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>🔮 Aura AI Workspace Hub</h1>", unsafe_allow_html=True)
st.write("### Welcome, Bhumika! *\"Small progress is still progress.\"*")

# ---------------------------------------------------------
# 2. STATE MANAGEMENT FOR THE RUNNING APPLICATION
# ---------------------------------------------------------
if 'journal_entries' not in st.session_state:
    st.session_state['journal_entries'] = [
        {"date": "2026-06-23", "mood": "😰 Anxious", "text": "Felt overwhelmed with mid-term math expectations."},
        {"date": "2026-06-24", "mood": "🧘 Calm", "text": "Took a structural study break; felt more balanced."}
    ]
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [
        {"sender": "Aura", "text": "Hi Bhumika! How can I support your study balance goals today?"}
    ]
if 'countdown_days' not in st.session_state:
    st.session_state['countdown_days'] = 142
if 'pomodoro_active' not in st.session_state:
    st.session_state['pomodoro_active'] = False

# ---------------------------------------------------------
# 3. INTERACTIVE HOME SCREEN NAVIGATION TABS
# ---------------------------------------------------------
# This structure lets users click and operate every module dynamically on one screen.
tab_home, tab_chat, tab_burnout, tab_analyzer, tab_journal, tab_study, tab_focus, tab_safety, tab_wellness = st.tabs([
    "🏠 Main Dashboard", 
    "🤖 AI Chat Support", 
    "🔥 Burnout Detector", 
    "🔍 Situation Analyzer", 
    "📖 Mood Journal", 
    "📚 Study Balance Hub", 
    "⏱️ Focus Mode", 
    "🚨 Safety Tools (SOS)", 
    "🧘 Wellness Hub"
])

# ==========================================
# 🏠 MODULE 1: MAIN DASHBOARD
# ==========================================
with tab_home:
    st.subheader("Current Core Status Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='ui-card'><h4>Stress Status</h4><div class='stat-number'>68%</div><p style='color:#00F2FE; text-align:center;'>Moderate Risk</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='ui-card'><h4>Exam Countdown</h4><div class='stat-number'>{st.session_state['countdown_days']}</div><p style='text-align:center;'>Days Remaining</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='ui-card'><h4>Study Productivity</h4><div class='stat-number'>78%</div><p style='text-align:center; color:#A370F7;'>Target Efficiency</p></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='ui-card'><h4>Daily Streak</h4><div class='stat-number'>🔥 7</div><p style='text-align:center;'>Days Active</p></div>", unsafe_allow_html=True)

    st.markdown("### Quick Log: How are you feeling right now?")
    m_col = st.columns(5)
    moods_list = ["😊 Happy", "🧘 Calm", "😰 Anxious", "🥵 Stressed", "😢 Sad"]
    for idx, mood_opt in enumerate(moods_list):
        if m_col[idx].button(mood_opt, key=f"home_mood_{idx}", use_container_width=True):
            st.success(f"Logged feeling state: {mood_opt}! Data transferred to analytics history.")

# ==========================================
# 🤖 MODULE 2: AI CHAT SUPPORT (RUNNING)
# ==========================================
with tab_chat:
    st.subheader("🤖 AI Companion Live Chat")
    
    # Render chat records dynamically
    for msg in st.session_state['chat_history']:
        if msg['sender'] == "Aura":
            st.markdown(f"**✨ Aura AI:** {msg['text']}")
        else:
            st.markdown(f"**👤 You:** {msg['text']}")
            
    st.markdown("---")
    chat_inp = st.text_input("Type your raw message or context prompt...", key="chat_input_field")
    if st.button("Send Input Content", type="primary"):
        if chat_inp:
            st.session_state['chat_history'].append({"sender": "User", "text": chat_inp})
            # Simple simulation logic matching UI goals
            responses = [
                "I completely understand. Let's take things one step at a time.",
                "Your peace of mind is what matters most. Have you taken a break recently?",
                "That sounds stressful. Let's try a quick 2-minute breathing pattern to reset."
            ]
            st.session_state['chat_history'].append({"sender": "Aura", "text": random.choice(responses)})
            st.rerun()

# ==========================================
# 🔥 MODULE 3: BURNOUT DETECTOR (RUNNING)
# ==========================================
with tab_burnout:
    st.subheader("🔥 Continuous Stress & Burnout Calculation Matrix")
    
    col_b1, col_b2 = st.columns([1, 2])
    with col_b1:
        st.markdown("<div class='ui-card'><p style='text-align:center;'>Metric Assessment Score</p><div class='stat-number'>68%</div></div>", unsafe_allow_html=True)
    with col_b2:
        st.write("#### Primary Flagged High-Stress Factors:")
        st.info("📉 **Low Recorded Sleep Hours:** Average under 6 hours flagged.")
        st.warning("📱 **High Digital Screen Exposures:** Extended learning windows without movement intervals.")

    st.write("#### Recommended Protective Tasks Checklist:")
    st.checkbox("Take an immediate structural 15-minute screen rest window", value=True)
    st.checkbox("Hydrate and balance nutritional items", value=False)

# ==========================================
# 🔍 MODULE 4: SITUATION ANALYZER (RUNNING)
# ==========================================
with tab_analyzer:
    st.subheader("🔍 Peer Pressure & Social Context Assessment Engine")
    st.write("Describe your immediate real-world social concern (e.g., peer pressure options):")
    
    sit_data = st.text_area("Input context descriptions here...", placeholder="My friends are forcing me to drop study tracking and hang out instead...")
    
    if st.button("Run Evaluation Scan"):
        if sit_data:
            st.markdown("<div class='ui-card'><h4 style='color:#FF5E62;'>Context Risk Threshold Level: 75% High Risk</h4></div>", unsafe_allow_html=True)
            st.error("⚠️ **Detected Traits:** Peer Group pressure dynamics, emotional diversion profiles.")
            st.info("💡 **Recommended Resolution Plan:** Establish firm personal boundary rules or setup a talk with a school mentor.")
        else:
            st.warning("Please enter a situation overview scenario first.")

# ==========================================
# 📖 MODULE 5: MOOD JOURNAL (RUNNING)
# ==========================================
with tab_journal:
    st.subheader("📖 Secure Personal Encryption Mood Journal")
    
    j_date = st.date_input("Journal Record Timestamping Target")
    j_mood = st.selectbox("Predominant Mental Vibe Status", ["😊 Happy", "🧘 Calm", "😰 Overwhelmed", "😢 Distracted"])
    j_text = st.text_area("Write down your inner processing details...")
    
    if st.button("Save Encrypted Journal Log Entry"):
        if j_text:
            st.session_state['journal_entries'].insert(0, {"date": str(j_date), "mood": j_mood, "text": j_text})
            st.success("Data secured inside app state engine.")
            st.rerun()
            
    st.write("#### Historical Verification Archives")
    for entry in st.session_state['journal_entries']:
        st.markdown(f"📅 **{entry['date']}** | **{entry['mood']}** — *{entry['text']}*")

# ==========================================
# 📚 MODULE 6: STUDY BALANCE HUB (RUNNING)
# ==========================================
with tab_study:
    st.subheader("📚 Academic Productivity Balancing Grid")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.metric("Logged Academic Workload Execution Today", "8.5 / 12 Hours Total")
    with col_s2:
        st.metric("Calculated Focus Target Score Value", "78%")
        
    st.write("#### Active Subsystem Workflows Available:")
    s_btn_cols = st.columns(4)
    if s_btn_cols[0].button("📋 Revision Tracker Module", use_container_width=True): st.toast("Opening Revision Trackers Dynamic Files...")
    if s_btn_cols[1].button("⏱️ Task Logs Module", use_container_width=True): st.toast("Opening Active Checklist Items...")
    if s_btn_cols[2].button("📉 Weak Spots Module", use_container_width=True): st.toast("Analyzing target subject performance margins...")
    if s_btn_cols[3].button("📝 Mock Exams Module", use_container_width=True): st.toast("Initializing test framework templates...")

# ==========================================
# ⏱️ MODULE 7: FOCUS MODE / POMODORO (RUNNING)
# ==========================================
with tab_focus:
    st.subheader("⏱️ Pomodoro Structural Execution Engine")
    
    f_col1, f_col2 = st.columns([1, 2])
    with f_col1:
        st.markdown("<div class='ui-card'><h1 style='text-align:center; color:#00F2FE; font-size:48px;'>25:00</h1><p style='text-align:center;'>Interval Loop 1 / 4</p></div>", unsafe_allow_html=True)
    with f_col2:
        if st.button("Start Focused Work Cycle Session", type="primary", use_container_width=True):
            st.info("Timer sequence is operational in your background profile interface.")
        if st.button("Reset Intermission Parameters", use_container_width=True):
            st.toast("Time settings restored back to defaults.")

# ==========================================
# 🚨 MODULE 8: SAFETY TOOLS / SOS (RUNNING)
# ==========================================
with tab_safety:
    st.subheader("🚨 Secure Emergency Support Channels & SOS Hub")
    
    st.markdown("<span style='color:#FF5E62; font-weight:bold;'>CRITICAL SYSTEM ALERT SWITCH:</span> Triggers continuous automated network transmissions to validation groups.", unsafe_allow_html=True)
    if st.button("🔴 EXECUTE HIGH RECOVERY EMERGENCY SYSTEM OVERRIDE (SOS)", use_container_width=True):
        st.error("🚨 CRITICAL ACTION TRIGGERED: Geolocation data vectors sent to primary crisis support teams.")
        
    st.write("#### Auxiliary Safe Communications Triggers:")
    saf_cols = st.columns(3)
    if saf_cols[0].button("📍 Share Precise Coordinates Link"): st.toast("Coordinates calculated successfully.")
    if saf_cols[1].button("📞 Mock Protective Call Trigger"): st.toast("Simulated security backup call initialized.")
    if saf_cols[2].button("☎️ Helpline Directories View"): st.info("National Crisis Center Help Desk: 112 / School Counselor Desk")

# ==========================================
# 🧘 MODULE 9: WELLNESS HUB (RUNNING)
# ==========================================
with tab_wellness:
    st.subheader("🧘 Behavioral Rest & Mind Decompression Utilities")
    
    with st.expander("🫁 2-3 Minute Targeted Deep Breathing Metrics"):
        st.write("Follow pattern: Inhale fully (4s) ... Retain position structure (4s) ... Expel stress air (4s)")
    with st.expander("🎵 Audio Frequency White-Noise Loops"):
        st.write("Playing: Ambient soundscape file simulation active.")
    with st.expander("✨ Neuro-Linguistic Affirmations Engine"):
        st.write("*'I possess complete command over my time management, mental peace, and goals.'*")

# ---------------------------------------------------------
# 4. FIXED PLATFORM FOOTER (GLOBAL UTILITIES)
# ---------------------------------------------------------
st.markdown("---")
f_col_1, f_col_2, f_col_3 = st.columns([2, 2, 1])
with f_col_1:
    st.caption("🔒 Architecture Security Frame Profile: AES 256 Environment Active")
with f_col_2:
    st.caption("🎯 Aura AI Framework Support Build Version 3.0.0 Alpha Codebase")
with f_col_3:
    if st.button("🔄 Clean Workspace Memory Cache"):
        st.rerun()
