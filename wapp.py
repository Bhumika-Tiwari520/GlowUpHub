import streamlit as st
import time
import pandas as pd
from datetime import datetime, timedelta

# ---------------------------------------------------------
# 1. PAGE CONFIG & NEON AESTHETIC STYLING (MATCHING MOCKUP)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Aura AI - Your Safe Space",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to mimic the exact dark-purple and glowing neon outline look from the mockup
st.markdown("""
<style>
    .stApp {
        background-color: #0B0C1E;
        color: #E0E2F5;
    }
    .main-header {
        text-align: center;
        padding: 15px;
        background: linear-gradient(90deg, #A370F7, #00F2FE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Stylized UI Card with Doodles/Icons */
    .doodle-card {
        background: #131535;
        border: 2px solid #2B2E63;
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(163, 112, 247, 0.2);
        position: relative;
    }
    .doodle-icon {
        font-size: 40px;
        margin-bottom: 10px;
    }
    .glow-text-cyan {
        color: #00F2FE;
        font-size: 32px;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(0, 242, 254, 0.6);
    }
    .glow-text-purple {
        color: #A370F7;
        font-size: 32px;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(163, 112, 247, 0.6);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>🔮 Aura AI - Safe Space & Study Partner</h1>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. PERSISTENT STATE MANAGEMENT
# ---------------------------------------------------------
if 'exams' not in st.session_state:
    st.session_state['exams'] = [
        {"name": "NDA Examination", "date": datetime(2026, 11, 15)},
        {"name": "Final Term Boards", "date": datetime(2027, 3, 1)}
    ]
if 'pomo_remaining' not in st.session_state:
    st.session_state['pomo_remaining'] = 25  # Set to 25 seconds for demonstration
if 'pomo_running' not in st.session_state:
    st.session_state['pomo_running'] = False

# ---------------------------------------------------------
# 3. INTERACTIVE PLATFORM TABS
# ---------------------------------------------------------
tab_home, tab_study, tab_focus, tab_chat, tab_burnout = st.tabs([
    "🏠 Main Dashboard", 
    "📚 Study Balance Hub", 
    "⏱️ Active Focus Timer", 
    "🤖 AI Chat Support", 
    "🔥 Burnout Detector"
])

# ==========================================
# 🏠 MODULE 1: MAIN DASHBOARD
# ==========================================
with tab_home:
    st.subheader("Welcome Back, Bhumika ✨")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="doodle-card">
            <div class="doodle-icon">🧘‍♀️</div>
            <h4>Mood Status</h4>
            <div class="glow-text-purple">Good Vibe</div>
            <p style="color: #8A8DBC; margin-top: 5px;">Your emotional baseline is stable today.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="doodle-card">
            <div class="doodle-icon">⚡</div>
            <h4>Stress Track</h4>
            <div class="glow-text-cyan">68%</div>
            <p style="color: #8A8DBC; margin-top: 5px;">Moderate load. Keep structural breaks active.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="doodle-card">
            <div class="doodle-icon">🔥</div>
            <h4>Daily Streak</h4>
            <div class="glow-text-purple">7 Days</div>
            <p style="color: #8A8DBC; margin-top: 5px;">Excellent consistency tracking!</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 📚 MODULE 2: STUDY BALANCE HUB (MULTI-EXAM)
# ==========================================
with tab_study:
    st.subheader("📚 Dynamic Exam Countdown Tracker")
    
    # Form to add custom examinations dynamically
    with st.expander("➕ Register and Target a New Examination"):
        with st.form("exam_form", clear_on_submit=True):
            exam_name = st.text_input("Examination Objective Name:")
            exam_date = st.date_input("Target Exam Date:")
            submit_exam = st.form_submit_button("Add Exam Tracking Card")
            if submit_exam and exam_name:
                st.session_state['exams'].append({"name": exam_name, "date": datetime.combine(exam_date, datetime.min.time())})
                st.success(f"Added {exam_name} to your tracking stack!")
                st.rerun()

    # Display dynamically generated countdown cards
    st.write("#### Your Active Deadlines:")
    grid_cols = st.columns(len(st.session_state['exams']) if st.session_state['exams'] else 1)
    
    for idx, exam in enumerate(st.session_state['exams']):
        time_diff = exam['date'] - datetime.now()
        days_left = max(0, time_diff.days)
        
        with grid_cols[idx % len(grid_cols)]:
            st.markdown(f"""
            <div class="doodle-card">
                <div class="doodle-icon">📅</div>
                <h4>{exam['name']}</h4>
                <div class="glow-text-cyan">{days_left} Days</div>
                <p style="color: #8A8DBC; font-size:12px;">Remaining until launch execution</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Remove {exam['name']}", key=f"del_{idx}"):
                st.session_state['exams'].pop(idx)
                st.rerun()

# ==========================================
# ⏱️ MODULE 3: ACTIVE FOCUS TIMER (LIVE TICKING)
# ==========================================
with tab_focus:
    st.subheader("⏱️ Real-Time Focus Clock")
    
    f_col1, f_col2 = st.columns([1, 2])
    
    with f_col1:
        # Show dynamic state countdown visually
        st.markdown(f"""
        <div class="doodle-card" style="text-align: center;">
            <div class="doodle-icon">⏳</div>
            <div class="glow-text-purple" style="font-size: 50px;">{st.session_state['pomo_remaining']}s</div>
            <p style="color: #8A8DBC;">Demonstration Window Loop</p>
        </div>
        """, unsafe_allow_html=True)
        
    with f_col2:
        st.write("#### Control Interface:")
        c1, c2 = st.columns(2)
        if c1.button("▶️ Start Focus Sequence", use_container_width=True):
            st.session_state['pomo_running'] = True
        if c2.button("⏸️ Reset Interval", use_container_width=True):
            st.session_state['pomo_running'] = False
            st.session_state['pomo_remaining'] = 25
            st.rerun()
            
    # Dynamic live ticking processing loop simulation
    if st.session_state['pomo_running'] and st.session_state['pomo_remaining'] > 0:
        time.sleep(1)
        st.session_state['pomo_remaining'] -= 1
        st.rerun()
    elif st.session_state['pomo_remaining'] == 0:
        st.balloons()
        st.success("🎉 Focus window finished! Time for a structural break.")
        st.session_state['pomo_running'] = False
        st.session_state['pomo_remaining'] = 25

# ==========================================
# 🤖 MODULE 4: AI CHAT SUPPORT
# ==========================================
with tab_chat:
    st.subheader("🤖 Interactive AI Companion")
    st.markdown("""
    <div class="doodle-card">
        <div class="doodle-icon">✨</div>
        <p><b>Aura AI:</b> Hi Bhumika! I'm here to help manage your study strategy and keep stress low. What's on your mind?</p>
    </div>
    """, unsafe_allow_html=True)
    st.text_input("Type your response message here...", key="chat_node_input")

# ==========================================
# 🔥 MODULE 5: BURNOUT DETECTOR
# ==========================================
with tab_burnout:
    st.subheader("🔥 Adaptive Risk Assessment Metrics")
    st.markdown("""
    <div class="doodle-card">
        <div class="doodle-icon">🛑</div>
        <h4>High Stress Vector Signal Detected</h4>
        <p>Screen time engagement trends run 23% higher than your standard healthy baselines. Consider enabling wellness breathing modes.</p>
    </div>
    """, unsafe_allow_html=True)
