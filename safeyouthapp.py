import streamlit as st
import time
import pandas as pd

# ---------------------------------------------------------
# 1. PAGE CONFIG & CUSTOM DARK NEON THEME (CSS)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Aura AI - Your Safe Space",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS injected to match the dark purple/blue theme of the image
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #0B0C1E;
        color: #E0E2F5;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #121432;
        border-right: 1px solid #2B2E63;
    }
    
    /* Custom Card styling */
    .aura-card {
        background: linear-gradient(145deg, #181A3A, #121432);
        border: 1px solid #323775;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* Metrics and Highlights */
    .highlight-purple {
        color: #A370F7;
        font-weight: bold;
    }
    .highlight-cyan {
        color: #00F2FE;
        font-weight: bold;
    }
    
    /* Custom circular/accent progress representation text */
    .stat-circle {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #00F2FE;
        margin: 10px 0;
        text-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
    }
    .stat-circle-orange {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #FF5E62;
        margin: 10px 0;
        text-shadow: 0 0 10px rgba(255, 94, 98, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. STATE MANAGEMENT INITIALIZATION
# ---------------------------------------------------------
if 'theme' not in st.session_state:
    st.session_state['theme'] = 'Galaxy'
if 'mood_history' not in st.session_state:
    st.session_state['mood_history'] = ['Good', 'Anxious', 'Calm', 'Good', 'Stressed']
if 'journal_entries' not in st.session_state:
    st.session_state['journal_entries'] = []

# ---------------------------------------------------------
# 3. SIDEBAR NAVIGATION CONTROLS (Mapping the 16 Screens)
# ---------------------------------------------------------
st.sidebar.title("🔮 Aura AI Navigation")
st.sidebar.caption("School Project Prototype Hub")

screen = st.sidebar.radio(
    "Go to Screen:",
    [
        "1. Splash & Welcome Screen",
        "2. Main Dashboard",
        "3. AI Chat Support",
        "4. Burnout Detector",
        "5. Situation Analyzer",
        "6. Mood Journal",
        "7. Study Balance Hub",
        "8. Focus Mode (Pomodoro)",
        "9. Safety Tools & SOS",
        "10. Wellness Hub",
        "11. Progress Insights",
        "12. Support Circle",
        "13. Trust & Safety (Privacy)",
        "14. Environment Shield & Ghost Mode",
        "15. Achievements & Streaks",
        "16. Global Settings"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Tip: Toggle through screens to demonstrate distinct application functions dynamically.")

# ---------------------------------------------------------
# 4. RENDER LOGIC FOR EACH UNIQUE SCREEN
# ---------------------------------------------------------

# --- SCREEN 1: SPLASH & WELCOME ---
if screen == "1. Splash & Welcome Screen":
    st.title("Welcome to Aura AI")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="aura-card">
            <h2>Aura AI</h2>
            <p><i>Your Safe Space. Your Growth Partner.</i></p>
            <hr style="border-color:#323775;">
            <ul>
                <li>✓ AI Emotional Support</li>
                <li>✓ Burnout Detection</li>
                <li>✓ Study Balance Planner</li>
                <li>✓ Safety & SOS Mode</li>
                <li>✓ Mood Journal</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Let's Begin 🚀", use_container_width=True):
            st.balloons()
            st.success("Welcome aboard! Use the sidebar navigation to explore features.")
            
    with col2:
        st.markdown("""
        <div class="aura-card" style="text-align: center;">
            <h3>Choose Your Theme 🌌</h3>
            <p>Pick a theme that makes you feel good.</p>
        </div>
        """, unsafe_allow_html=True)
        theme_choice = st.selectbox("Active Theme", ["Galaxy", "Lavender", "Ocean", "Mint", "Sunset"], index=0)
        st.session_state['theme'] = theme_choice
        st.write(f"Current selection saved: **{theme_choice}**")

# --- SCREEN 2: MAIN DASHBOARD ---
elif screen == "2. Main Dashboard":
    st.title("Good Evening, Bhumika 👋")
    st.caption("“Small progress is still progress.”")
    
    st.subheader("How are you feeling today?")
    mood = st.columns(5)
    moods = ["😊 Happy", "🧘 Calm", "😰 Anxious", "🥵 Stressed", "😢 Sad"]
    for i, m in enumerate(moods):
        if mood[i].button(m, use_container_width=True):
            st.toast(f"Logged feeling: {m}")

    st.markdown("---")
    st.subheader("Quick Access Dashboard Grid")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="aura-card"><h4>🤖 AI Chat Support</h4><p>Instant Conversational Help</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="aura-card"><h4>⏱️ Focus Mode</h4><p>Pomodoro Work Timer</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="aura-card"><h4>📖 Mood Journal</h4><p>Log Your Daily Experiences</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="aura-card"><h4>🔥 Burnout Tracker</h4><p>Analyze Stress Thresholds</p></div>', unsafe_allow_html=True)

# --- SCREEN 3: AI CHAT SUPPORT ---
elif screen == "3. AI Chat Support":
    st.title("🤖 AI Support Chat")
    st.caption("How can I support you today?")
    
    # Mock Chat History Container
    st.markdown("""
    <div class="aura-card">
        <p><b>✨ Aura AI:</b> Hi Bhumika! How can I support you today?</p>
        <p style='color: #A370F7;'><b>👤 You:</b> I'm feeling stressed about my examinations.</p>
        <p><b>✨ Aura AI:</b> I completely understand. Let's take things one step at a time. What's worrying you the most right now?</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fast prompt pills
    pills = st.columns(4)
    if pills[0].button("Need Motivation", use_container_width=True): user_msg = "Need Motivation"
    if pills[1].button("Need Study Plan", use_container_width=True): user_msg = "Need Study Plan"
    if pills[2].button("Need To Vent", use_container_width=True): user_msg = "Need To Vent"
    if pills[3].button("Calm Me Down", use_container_width=True): user_msg = "Calm Me Down"
    
    chat_input = st.text_input("Type your message here...", key="chat_in")
    if st.button("Send Message", type="primary"):
        st.info("Prototype response simulation: Aura AI is processing your mood parameters...")

# --- SCREEN 4: BURNOUT DETECTOR ---
elif screen == "4. Burnout Detector":
    st.title("🔥 Burnout Detector")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="aura-card"><p style="text-align:center;">Your Stress Level</p><div class="stat-circle">68%</div><p style="text-align:center; color:#00F2FE;">Moderate Stress</p></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="aura-card">
            <h4>Primary Stress Contributors</h4>
            <ul>
                <li>🛑 <b>Low Sleep metrics:</b> Under 6 hours documented</li>
                <li>📱 <b>High Screen Time:</b> Increased continuous exposure</li>
                <li>📚 <b>Long Study Sessions:</b> Insufficient breakdown breaks</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.subheader("Personalized System Suggestions")
    st.checkbox("Take a short structural 15-minute break", value=True)
    st.checkbox("Hydrate Yourself immediately", value=False)
    st.checkbox("Walk outside for 10 Minutes", value=False)

# --- SCREEN 5: SITUATION ANALYZER ---
elif screen == "5. Situation Analyzer":
    st.title("🔍 Situation Analyzer")
    st.write("Describe the exact real-world scenario or peer pressure event currently bothersome to you:")
    
    situation_text = st.text_area("Situation Entry Box", placeholder="My friends are forcing me to skip study tracking sessions and go out hang around...")
    
    if st.button("Run Analytical Evaluation", type="primary"):
        with st.spinner("Processing social matrix metrics..."):
            time.sleep(1)
        st.markdown('<div class="aura-card"><p>Analysis Risk Status Match</p><div class="stat-circle-orange">75%</div><p style="text-align:center; color:#FF5E62;">High Social Risk Context Detected</p></div>', unsafe_allow_html=True)
        
        st.warning("⚠️ **Detected Factors:** Peer Pressure, Emotional Manipulation tendencies.")
        st.info("💡 **Suggested Remedial Action:** Construct clear personal boundaries or seek consultation from a Trusted Adult / School Counselor.")

# --- SCREEN 6: MOOD JOURNAL ---
elif screen == "6. Mood Journal":
    st.title("📖 Daily Mood Journal")
    
    entry_date = st.date_input("Journal Entry Date")
    mood_emoji = st.selectbox("Dominant Emotional State", ["😊 Happy", "🧘 Balanced/Calm", "😰 Anxious/Overwhelmed", "🥵 Burned Out"])
    journal_text = st.text_area("Write down your thoughts details...", height=150)
    
    if st.button("Save Journal Entry"):
        st.session_state['journal_entries'].append({"date": entry_date, "mood": mood_emoji, "text": journal_text})
        st.success("Entry compiled and safely encrypted in system storage memory!")
        
    if st.session_state['journal_entries']:
        st.subheader("Previous Validated Entries")
        for entry in st.session_state['journal_entries']:
            st.markdown(f"**{entry['date']}** ({entry['mood']}): {entry['text']}")

# --- SCREEN 7: STUDY BALANCE HUB ---
elif screen == "7. Study Balance Hub":
    st.title("📚 Study Balance Hub")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="NDA Examination Target Countdown", value="142 Days Remaining")
        st.progress(0.78, text="Target Routine Efficiency Focus Score: 78%")
    with col2:
        st.markdown("""
        <div class="aura-card">
            <h4>Today's Study Allocation Tracking</h4>
            <h3><b>8.5 / 12 Hours Logged</b></h3>
        </div>
        """, unsafe_allow_html=True)
        
    st.subheader("Academic Utility Modules Checklists")
    cb1, cb2, cb3, cb4 = st.columns(4)
    cb1.button("📋 Revision Tracker")
    cb2.button("⏱️ Daily Tasks Management")
    cb3.button("📉 Weak Topics Review")
    cb4.button("📝 Mock Exam Setup")

# --- SCREEN 8: FOCUS MODE (POMODORO) ---
elif screen == "8. Focus Mode (Pomodoro)":
    st.title("⏱️ Focus Mode & Time Allocation")
    st.write("Pomodoro Session Configuration Setup:")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="aura-card" style="text-align:center;"><h1 style="font-size:60px; color:#00F2FE;">25:00</h1><p>Session Allocation 1 / 4</p></div>', unsafe_allow_html=True)
    with col2:
        st.write("Click below to start your deep structural session execution:")
        if st.button("Start Timer", type="primary", use_container_width=True):
            st.info("Timer counting down silently in your background environment profile.")
        if st.button("Reset Focus Windows", use_container_width=True):
            st.toast("Timer reset completed.")
            
    st.caption("✨ *Take short breaks to ensure performance consistency!*")

# --- SCREEN 9: SAFETY TOOLS & SOS ---
elif screen == "9. Safety Tools & SOS":
    st.title("🚨 Emergency Safety Configuration Matrix")
    
    st.error("🚨 **SOS Trigger Action:** Emergency Help protocols instantly alert primary system contacts.")
    if st.button("🔴 EXECUTE IMMEDIATE SOS ALERT SYSTEM", use_container_width=True):
        st.error("CRITICAL ALERTS TRANSMITTED TO PRIMARY EMERGENCY TRACKING CHANNELS!")
        
    c1, c2, c3, c4 = st.columns(4)
    c1.button("📍 Share Precise GPS Locations")
    c2.button("📞 Generate Fake Security Inbound Call")
    c3.button("💬 Send Silent Security SMS Data")
    c4.button("☎️ National Safety Helpline Numbers")

# --- SCREEN 10: WELLNESS HUB ---
elif screen == "10. Wellness Hub":
    st.title("🧘 Behavioral Wellness & Mental Care Hub")
    
    st.markdown("""
    Select an optimized decompression workflow activity to normalize metrics:
    """)
    
    with st.expander("🫁 Deep Breathing Exercises (2-3 Minutes run)"):
        st.write("Inhale deep through nose... Hold context position... Exhale smooth...")
    with st.expander("🧘 Target Mental Mindfulness Meditation Guides"):
        st.write("Audio simulation placeholder: Calming guidance tracker active.")
    with st.expander("🎵 Ambient Stress Relaxing Soundscapes"):
        st.write("Playing natural soft white-noise dynamic frequencies.")
    with st.expander("✨ Positive Psychological Affirmations Engine"):
        st.write("*'I am entirely capable of managing my exams and maintaining clear internal peace.'*")

# --- SCREEN 11: PROGRESS INSIGHTS ---
elif screen == "11. Progress Insights":
    st.title("📉 Continuous Progress & Trend Optimization Insights")
    
    time_frame = st.radio("Analytics Aggregation Scale:", ["Week View", "Month View", "Year Analysis View"], horizontal=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Mood Average Scale", "Good (Stable Status)")
    col2.metric("Study Routine Balance", "72% Efficiency Score")
    col3.metric("Self Care Optimization Metric", "80% Compliance Value")
    
    st.write("📊 **System Metric Trend Over Current Week Span:**")
    chart_data = pd.DataFrame([4, 6, 5, 7, 5, 8, 9], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], columns=['System Wellness Value Score'])
    st.line_chart(chart_data)

# --- SCREEN 12: SUPPORT CIRCLE ---
elif screen == "12. Support Circle":
    st.title("👥 Your Trusted Support Circle")
    st.write("You are completely safe. Connect immediately with validated personal care resources:")
    
    st.markdown("""
    <div class="aura-card">
        <ul>
            <li>❤️ <b>Best Friend Support Node:</b> +91 98765 43210</li>
            <li>🏫 <b>Assigned School Counsellor Support Officer:</b> +91 91234 56789</li>
            <li>👩‍🏫 <b>Primary Mentor Contact (Ritika Ma'am):</b> +91 99887 76585</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("➕ Register New Contact Node Profile"):
        st.info("Input tracking prompt simulator triggered.")

# --- SCREEN 13: TRUST & SAFETY (PRIVACY) ---
elif screen == "13. Trust & Safety (Privacy)":
    st.title("🛡️ Trust, Privacy, & Verification Settings")
    
    st.markdown("""
    <div class="aura-card">
        <h4>Privacy Control Framework Settings</h4>
        <p>Your ultimate personal interface protection system overview details.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("🔍 Audit Profile System Metadata Collection Parameters")
    st.button("📦 Export Personal User Encrypted Package System Data")
    st.button("🗑️ PURGE ALL INTERNAL PROFILE DATA SETS PERMANENTLY", type="secondary")

# --- SCREEN 14: ENVIRONMENT SHIELD & GHOST MODE ---
elif screen == "14. Environment Shield & Ghost Mode":
    st.title("🛡️ Environment Shield & Stealth App Concealment")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="aura-card">
            <h4>Environment Noise Shield Active</h4>
            <p>We actively monitor structural surrounding noise metrics to ensure study atmosphere health parameters.</p>
        </div>
        """, unsafe_allow_html=True)
        st.toggle("Activate Noise Shield Monitoring", value=True)
        
    with col2:
        st.markdown("""
        <div class="aura-card">
            <h4>Ghost App Camouflage Mode</h4>
            <p>Conceal app interface appearance to mimic regular utility calculators on screen checks.</p>
        </div>
        """, unsafe_allow_html=True)
        st.toggle("Enable Stealth Ghost Screen Trigger", value=False)

# --- SCREEN 15: ACHIEVEMENTS & STREAKS ---
elif screen == "15. Achievements & Streaks":
    st.title("🏆 Gamified Behavioral Milestone Tracking")
    
    st.markdown('<div class="aura-card" style="text-align:center;"><h1>🔥 7 Days Streak</h1><p>Consistent daily mental wellness verification actions logged.</p></div>', unsafe_allow_html=True)
    
    st.subheader("Unlocked System Badges Ecosystem")
    b1, b2, b3 = st.columns(3)
    b1.markdown("🎯 **Focus Master:** Pomodoro milestone achieved.")
    b2.markdown("🦅 **Early Bird Routine:** Mindful tasks logged before 7 AM.")
    b3.markdown("⭐ **Self Care Star:** High consistency rating.")

# --- SCREEN 16: GLOBAL SETTINGS ---
elif screen == "16. Global Settings":
    st.title("⚙️ Global Master Configuration Parameters")
    
    st.selectbox("System Theme Workspace Setting", ["Galaxy Theme Dark Mode", "Bright Daylight Alternative Setup"], key="glob_theme")
    st.toggle("System Level Push Notifications Dispatcher", value=True)
    st.selectbox("Default Linguistic Localization Selection", ["English (US/UK Core UI)", "Hindi System Translation Module"])
    
    st.markdown("---")
    st.caption("Aura AI Engine Architecture Framework Integration Prototype Version: v3.0.0 Alpha Production Build")
