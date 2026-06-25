import streamlit as st

def init_session():

    defaults = {
        "theme":"Galaxy",
        "mood":"Happy",
        "chat_history":[],
        "journal_entries":[],
        "focus_time":25,
        "study_score":72
    }

    for key,value in defaults.items():
        if key not in st.session_state:
            st.session_state[key]=value
moods = [
    "😊 Happy",
    "😌 Calm",
    "😟 Anxious",
    "😩 Stressed",
    "😢 Sad"
]

quick_features = [
    "🤖 AI Chat",
    "🎯 Focus Mode",
    "📔 Journal",
    "🔥 Burnout Detector",
    "🛡 Safety Tools",
    "🌿 Wellness Hub",
    "📚 Study Balance",
    "📊 Progress"]
def glass_card(title, value):

    st.markdown(f"""
    <div class='glow-card'>
        <h4>{title}</h4>
        <h2>{value}</h2>
    </div>
    """, unsafe_allow_html=True)
from streamlit_option_menu import option_menu
import streamlit as st

def navbar():

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Journal",
            "Focus",
            "Progress",
            "Profile"
        ],
        icons=[
            "house",
            "book",
            "bullseye",
            "bar-chart",
            "person"
        ],
        orientation="horizontal"
    )

    return selected
import plotly.graph_objects as go

def mood_chart():

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
            y=[4,5,3,6,5,7,6],
            mode="lines+markers"
        )
    )

    fig.update_layout(
        paper_bgcolor="#101a35",
        plot_bgcolor="#101a35",
        font_color="white",
        height=300
    )

    return fig
import streamlit as st

st.set_page_config(
    page_title="Aura AI",
    page_icon="💜",
    layout="wide"
)

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

if "started" not in st.session_state:
    st.session_state.started = False

if "welcome" not in st.session_state:
    st.session_state.welcome = False

if "theme" not in st.session_state:
    st.session_state.theme = "Galaxy"

# SPLASH SCREEN

if not st.session_state.started:

    st.markdown("""
    <div class='hero'>
        <h1>💜 Aura AI</h1>
        <p>Your Safe Space. Your Growth Partner.</p>
    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,2,1])

    with col2:
        if st.button("Get Started"):
            st.session_state.started = True
            st.rerun()

    st.stop()

# WELCOME SCREEN

if not st.session_state.welcome:

    st.markdown("""
    <div class='glass'>
    <h2>👋 Welcome to Aura AI</h2>

    <ul>
    <li>AI Emotional Support</li>
    <li>Burnout Detection</li>
    <li>Study Balance Planner</li>
    <li>Safety SOS Mode</li>
    <li>Mood Journal</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    if st.button("Let's Begin"):
        st.session_state.welcome = True
        st.rerun()

    st.stop()

# THEME SELECTION

st.title("🎨 Choose Your Theme")

theme = st.radio(
    "",
    [
        "Lavender",
        "Ocean",
        "Mint",
        "Peach",
        "Sunset",
        "Galaxy"
    ],
    horizontal=True
)

st.session_state.theme = theme

st.success(f"Theme Selected: {theme}")

st.divider()

st.markdown("""
### 🚀 Aura AI Dashboard

Use the sidebar to access:

- AI Chat
- Mood Journal
- Study Balance
- Focus Mode
- Safety Tools
- Wellness Hub
- Progress Insights
- Privacy Dashboard
- Achievements
- Settings
""")
import streamlit as st
from utils.data import moods, quick_features
from components.charts import mood_chart

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🌙 Good Evening, Bhumika 💜")

st.caption("Small progress is still progress.")

mood = st.selectbox(
    "How are you feeling today?",
    moods
)

st.session_state.mood = mood

st.subheader("Quick Access")

c1,c2,c3,c4 = st.columns(4)

for i,feature in enumerate(quick_features[:4]):
    [c1,c2,c3,c4][i].button(feature)

c5,c6,c7,c8 = st.columns(4)

for i,feature in enumerate(quick_features[4:]):
    [c5,c6,c7,c8][i].button(feature)

st.divider()

left,right = st.columns([1,1])

with left:

    st.metric(
        "Mood Average",
        "Good 😊"
    )

    st.metric(
        "Study Balance",
        "72%"
    )

with right:

    st.plotly_chart(
        mood_chart(),
        use_container_width=True)
st.set_page_config(layout="wide")

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🤖 AI Support Chat")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"""
        <div class='chat-box'>
        👤 <b>You:</b><br>{msg}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='chat-box'>
        🤖 <b>Aura AI:</b><br>{msg}
        </div>
        """, unsafe_allow_html=True)

message = st.chat_input("Type your message...")

if message:

    st.session_state.chat_history.append(("user", message))

    response = f"""
I understand.

You said:
'{message}'

Take a deep breath and focus on one small step at a time.
You are making progress 💜
"""

    st.session_state.chat_history.append(("ai", response))

    st.rerun()

st.divider()

c1,c2,c3,c4 = st.columns(4)

with c1:
    if st.button("Need Motivation"):
        st.session_state.chat_history.append(
            ("ai","You have survived every difficult day so far 💜")
        )

with c2:
    if st.button("Need Study Plan"):
        st.session_state.chat_history.append(
            ("ai","Study 25 mins → Break 5 mins → Repeat")
        )

with c3:
    if st.button("Need To Vent"):
        st.session_state.chat_history.append(
            ("ai","I'm listening. Tell me what happened.")
        )

with c4:
    if st.button("Calm Me Down"):
        st.session_state.chat_history.append(
            ("ai","Try 4-4-4 breathing for one minute.")
        )
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📔 Mood Journal")

if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

mood = st.selectbox(
    "Today's Mood",
    ["😊 Happy","😌 Calm","😟 Anxious","😩 Stressed","😢 Sad"]
)

entry = st.text_area(
    "Write your thoughts..."
)

if st.button("Save Entry"):

    st.session_state.journal_entries.append(
        {
            "Mood": mood,
            "Entry": entry
        }
    )

    st.success("Entry Saved")

st.divider()

st.subheader("Previous Entries")

if st.session_state.journal_entries:

    df = pd.DataFrame(
        st.session_state.journal_entries
    )

    st.dataframe(df,use_container_width=True)

else:
    st.info("No journal entries yet.")

st.divider()

st.subheader("AI Summary")

if st.session_state.journal_entries:

    latest = st.session_state.journal_entries[-1]

    st.markdown(f"""
### Summary

Mood: {latest['Mood']}

The entry suggests you may benefit from:

✅ Small breaks

✅ Hydration

✅ Positive self-talk

✅ Balanced study sessions
""")
import streamlit as st
import random

st.set_page_config(layout="wide")

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🧠 Situation Analyzer")

situation = st.text_area(
    "Describe the situation bothering you..."
)

col1,col2 = st.columns(2)

with col1:
    st.button("🎤 Voice Input")

with col2:
    analyze = st.button("Analyze Situation")

if analyze:

    confidence = random.randint(70,95)
    risk = random.randint(30,85)

    st.metric(
        "Confidence Score",
        f"{confidence}%"
    )

    st.metric(
        "Risk Level",
        f"{risk}%"
    )

    if risk > 70:
        st.error("High Risk Situation")

    elif risk > 40:
        st.warning("Moderate Risk")

    else:
        st.success("Low Risk")

    st.markdown("""
### Suggestions

• Set clear boundaries

• Talk to someone trusted

• Avoid impulsive decisions

• Take a short break before responding
""")
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🔥 Burnout Detector")

sleep = st.slider(
    "Sleep Hours",
    0,12,6
)

screen = st.slider(
    "Screen Time",
    0,15,8
)

study = st.slider(
    "Study Hours",
    0,15,7
)

burnout = int(
    ((15-screen)*2 +
    study*4 +
    (8-sleep)*5)
)

burnout = max(0,min(100,burnout))

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=burnout,
    title={"text":"Stress Level"}
))

fig.update_layout(
    paper_bgcolor="#101a35",
    font_color="white",
    height=400
)

st.plotly_chart(
    fig,
    use_container_width=True
)

if burnout > 70:

    st.error("High Burnout Risk")

elif burnout > 40:

    st.warning("Moderate Burnout Risk")

else:

    st.success("Healthy Stress Level")

st.markdown("""
### Recommendations

✅ Take a break

✅ Drink water

✅ Walk 10 minutes

✅ Sleep earlier

✅ Reduce screen exposure
""")
quick_features = [
"🤖 AI Chat",
"🧠 Situation Analyzer",
"🔥 Burnout Detector",
"📔 Mood Journal",
"🎯 Focus Mode",
"🛡 Safety Tools",
"🌿 Wellness Hub",
"📊 Progress Insights"
]
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📚 Study Balance Hub")

col1,col2,col3,col4 = st.columns(4)

with col1:
    study_hours = st.number_input(
        "Daily Study Hours",
        0,
        15,
        6
    )

with col2:
    revision = st.slider(
        "Revision %",
        0,
        100,
        65
    )

with col3:
    mock_score = st.slider(
        "Mock Test Score",
        0,
        100,
        72
    )

with col4:
    focus = st.slider(
        "Focus Score",
        0,
        100,
        80
    )

balance_score = int(
    (revision + mock_score + focus)/3
)

st.metric(
    "Study Balance Score",
    f"{balance_score}%"
)

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=balance_score,
    title={"text":"Overall Performance"}
))

fig.update_layout(
    paper_bgcolor="#101a35",
    font_color="white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Today's Tasks")

task1 = st.checkbox("Complete NDA Mathematics")
task2 = st.checkbox("Current Affairs Revision")
task3 = st.checkbox("English Practice")
task4 = st.checkbox("Mock Test")

completed = sum([task1,task2,task3,task4])

st.progress(completed/4)

st.success(
    f"{completed}/4 Tasks Completed"
)
import streamlit as st
import time

st.set_page_config(layout="wide")

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🎯 Focus Mode")

if "pomodoro" not in st.session_state:
    st.session_state.pomodoro = 25

minutes = st.slider(
    "Focus Minutes",
    5,
    60,
    25
)

st.session_state.pomodoro = minutes

st.metric(
    "Current Session",
    f"{minutes} Minutes"
)

col1,col2,col3 = st.columns(3)

with col1:
    start = st.button("▶ Start")

with col2:
    pause = st.button("⏸ Pause")

with col3:
    reset = st.button("🔄 Reset")

if start:

    progress = st.progress(0)

    for i in range(minutes*60):

        progress.progress(
            (i+1)/(minutes*60)
        )

        time.sleep(1)

st.divider()

st.subheader("Focus Tips")

st.markdown("""
✅ Keep phone away

✅ Study in blocks

✅ Drink water

✅ Take short breaks

✅ Track distractions
""")
import streamlit as st

st.set_page_config(layout="wide")

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🛡 Safety Tools")

st.warning(
    "Emergency features are demo placeholders."
)

c1,c2 = st.columns(2)

with c1:

    if st.button("🚨 SOS Emergency"):
        st.error(
            "SOS Triggered (Demo)"
        )

    if st.button("📍 Share Location"):
        st.success(
            "Location Shared (Demo)"
        )

with c2:

    if st.button("📞 Fake Call"):
        st.info(
            "Incoming Call Generated (Demo)"
        )

    if st.button("📨 Emergency SMS"):
        st.success(
            "SMS Sent (Demo)"
        )

st.divider()

st.subheader("Trusted Contacts")

name = st.text_input(
    "Contact Name"
)

phone = st.text_input(
    "Phone Number"
)

if st.button("Add Contact"):

    st.success(
        f"{name} Added"
    )

st.divider()

st.subheader("Helpline Numbers")

st.info("""
Women Helpline: 1091

Emergency: 112

Child Helpline: 1098
""")
import streamlit as st

st.set_page_config(layout="wide")

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🌿 Wellness Hub")

tab1,tab2,tab3,tab4 = st.tabs([
    "Breathing",
    "Meditation",
    "Affirmations",
    "Music"
])

with tab1:

    st.subheader(
        "4-4-4 Breathing"
    )

    st.markdown("""
1. Inhale 4 seconds

2. Hold 4 seconds

3. Exhale 4 seconds

Repeat 5 times.
""")

with tab2:

    st.subheader(
        "Quick Meditation"
    )

    st.markdown("""
Sit comfortably.

Close your eyes.

Focus on breathing.

Observe thoughts without judging them.
""")

with tab3:

    affirmations = [
        "I am improving every day.",
        "I can handle challenges.",
        "My effort matters.",
        "I deserve rest and balance."
    ]

    for item in affirmations:
        st.success(item)

with tab4:

    st.info(
        "Relaxing music player can be integrated later."
    )

st.divider()

st.subheader("Support Circle")

friend = st.text_input(
    "Friend / Mentor Name"
)

if st.button("Add Support Person"):

    st.success(
        f"{friend} Added"
    )
c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Mood Score",
        "84%"
    )

with c2:
    st.metric(
        "Focus Score",
        "78%"
    )

with c3:
    st.metric(
        "Study Balance",
        "81%"
    )

with c4:
    st.metric(
        "Burnout Risk",
        "32%"
    )
import streamlit as st
import plotly.express as px
import pandas as pd

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📊 Progress Insights")

df = pd.DataFrame({
    "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "Mood":[6,7,5,8,7,9,8],
    "Focus":[7,8,6,8,7,9,8],
    "Study":[5,6,7,8,7,8,9]
})

fig = px.line(
    df,
    x="Day",
    y=["Mood","Focus","Study"],
    markers=True
)

fig.update_layout(
    paper_bgcolor="#101a35",
    plot_bgcolor="#101a35",
    font_color="white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

col1,col2,col3 = st.columns(3)

with col1:
    st.metric("Weekly Mood", "82%")

with col2:
    st.metric("Focus Trend", "79%")

with col3:
    st.metric("Study Growth", "+14%")

st.subheader("AI Summary")

st.success("""
You maintained a consistent focus level this week.

Study balance is improving.

Stress indicators remained moderate.
""")
import streamlit as st

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🔒 Privacy Dashboard")

st.subheader("Data Controls")

save_history = st.toggle(
    "Save Chat History",
    value=True
)

save_journal = st.toggle(
    "Save Journal Entries",
    value=True
)

analytics = st.toggle(
    "Allow Analytics",
    value=False
)

st.divider()

st.subheader("Ghost Mode")

ghost = st.toggle(
    "Enable Ghost Mode"
)

if ghost:
    st.success(
        "Ghost Mode Activated"
    )

st.divider()

st.subheader("Quick Hide")

if st.button("Hide Screen"):
    st.info(
        "Privacy Screen Enabled"
    )

st.divider()

if st.button("Delete My Data"):
    st.warning(
        "All local data cleared (demo)"
    )
import streamlit as st

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🏆 Achievements")

badges = [
    "🌱 First Journal",
    "🔥 3 Day Streak",
    "📚 Study Warrior",
    "💜 Mood Master",
    "🎯 Focus Champion",
    "🛡 Safety Aware",
    "🌿 Wellness Explorer"
]

for badge in badges:

    st.markdown(f"""
    <div class='glow-card'>
        <h3>{badge}</h3>
    </div>
    <br>
    """, unsafe_allow_html=True)

st.subheader("Rewards")

st.metric(
    "Trees Planted",
    "12 🌳"
)

st.metric(
    "XP Points",
    "1450"
)
import streamlit as st

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("⚙ Settings")

theme = st.selectbox(
    "Theme",
    [
        "Galaxy",
        "Lavender",
        "Ocean",
        "Mint",
        "Peach",
        "Sunset"
    ]
)

language = st.selectbox(
    "Language",
    [
        "English",
        "Hindi"
    ]
)

notifications = st.toggle(
    "Notifications",
    value=True
)

reminders = st.toggle(
    "Daily Reminder",
    value=True
)

st.success(
    f"{theme} Theme Selected"
)
import streamlit as st

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🚀 All Features")

features = [
    "🤖 AI Chat",
    "🧠 Situation Analyzer",
    "🔥 Burnout Detector",
    "📔 Mood Journal",
    "📚 Study Balance",
    "🎯 Focus Mode",
    "🛡 Safety Tools",
    "🌿 Wellness Hub",
    "📊 Analytics",
    "🔒 Privacy",
    "🏆 Achievements",
    "⚙ Settings"
]

cols = st.columns(3)

for i,feature in enumerate(features):
    with cols[i % 3]:
        st.markdown(f"""
        <div class='quick-card'>
            <h3>{feature}</h3>
        </div>
        <br>
        """, unsafe_allow_html=True)
import streamlit as st

def init_session():

    defaults = {
        "theme":"Galaxy",
        "chat_history":[],
        "journal_entries":[]
    }

    for k,v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v.theme-galaxy{
background:#050816;
}

.theme-lavender{
background:#2b1e3f;
}

.theme-ocean{
background:#071d2e;
}

.theme-mint{
background:#0d2c24;
}

.theme-peach{
background:#3a241d;
}

.theme-sunset{
background:#2d1424;
}
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
    background:
    radial-gradient(circle at top right,
    rgba(128,0,255,.25),
    transparent 25%),
    linear-gradient(
    180deg,
    #050816 0%,
    #071124 50%,
    #0a1020 100%
    );

    color:white;
}

/* Hide Streamlit Elements */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* Glass Cards */

.glass-card{
    background:rgba(255,255,255,.05);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,.08);

    border-radius:24px;

    padding:24px;

    box-shadow:
    0 0 30px rgba(139,92,246,.18);
}

/* Metric Cards */

.metric-card{

    background:#0f1730;

    border-radius:24px;

    padding:20px;

    text-align:center;

    transition:.3s;

    border:1px solid rgba(168,85,247,.15);
}

.metric-card:hover{

    transform:translateY(-5px);

    box-shadow:
    0 0 35px rgba(168,85,247,.35);
}

.metric-number{

    font-size:32px;

    color:#c084fc;

    font-weight:700;
}

.metric-title{

    color:#9ca3af;
}

/* Hero */

.hero-title{

    font-size:48px;

    font-weight:700;

    color:white;
}

.hero-highlight{

    color:#c084fc;
}

.hero-sub{

    color:#9ca3af;
}

/* Buttons */

.stButton > button{

    width:100%;

    border-radius:18px;

    background:
    linear-gradient(
    90deg,
    #7c3aed,
    #a855f7
    );

    color:white;

    border:none;

    height:48px;

    font-weight:600;
}

/* Quick Cards */

.quick-card{

    background:#111b36;

    border-radius:22px;

    padding:22px;

    text-align:center;

    transition:.3s;
}

.quick-card:hover{

    transform:translateY(-6px);

    box-shadow:
    0px 0px 35px rgba(124,58,237,.45);
}

/* Chat */

.chat-user{

    background:#1d2542;

    border-radius:20px;

    padding:15px;

    margin-bottom:10px;
}

.chat-ai{

    background:#12192f;

    border-radius:20px;

    padding:15px;

    margin-bottom:10px;
}
import streamlit as st
import plotly.express as px
import pandas as pd

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# HERO

st.markdown("""
<div class='glass-card'>

<h1 class='hero-title'>
Welcome Back
<span class='hero-highlight'>💜</span>
</h1>

<p class='hero-sub'>
Your emotional wellness and study companion.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# METRICS

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='metric-card'>
    <div class='metric-title'>Mood Score</div>
    <div class='metric-number'>84%</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-card'>
    <div class='metric-title'>Focus</div>
    <div class='metric-number'>78%</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-card'>
    <div class='metric-title'>Balance</div>
    <div class='metric-number'>81%</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='metric-card'>
    <div class='metric-title'>Stress</div>
    <div class='metric-number'>32%</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# QUICK FEATURES

st.subheader("Quick Assist")

features = [
"🤖 AI Chat",
"🧠 Analyzer",
"🔥 Burnout",
"📔 Journal",
"🎯 Focus",
"📚 Study",
"🛡 Safety",
"🌿 Wellness"
]

cols = st.columns(4)

for i,item in enumerate(features):

    with cols[i % 4]:

        st.markdown(f"""
        <div class='quick-card'>
        <h3>{item}</h3>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# CHART

data = pd.DataFrame({
"Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
"Mood":[6,7,5,8,7,9,8]
})

fig = px.area(
    data,
    x="Day",
    y="Mood"
)

fig.update_layout(
paper_bgcolor="#111827",
plot_bgcolor="#111827",
font_color="white"
)

st.plotly_chart(
fig,
use_container_width=True
)

# DAILY MOTIVATION

st.success(
"✨ Progress is progress, no matter how small."
)
st.sidebar.markdown("""
# 💜 Aura AI

### Your Growth Companion
""")
mood = st.select_slider(
"Today's Mood",
options=[
"😢",
"😟",
"😐",
"😊",
"😁"
]
)

st.info(f"Current Mood: {mood}")
from datetime import date

exam_date = date(2027,4,15)

today = date.today()

days_left = (exam_date - today).days

st.metric(
"⏳ NDA Countdown",
f"{days_left} Days"
)
from datetime import date

exam_date = date(2027,4,15)

today = date.today()

days_left = (exam_date - today).days

st.metric(
"⏳ NDA Countdown",
f"{days_left} Days"
)
from datetime import date

exam_date = date(2027,4,15)

today = date.today()

days_left = (exam_date - today).days

st.metric(
"⏳ NDA Countdown",
f"{days_left} Days"
)
go.Indicator(
mode="gauge+number+delta"
)
st.markdown("""
<div class='glass-card'>
<h3>🤖 Aura Assistant</h3>

Need help?

• Study Planning

• Stress Management

• Daily Motivation

• Safety Guidance

</div>
""", unsafe_allow_html=True)
