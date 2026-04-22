import streamlit as st
import random

# Page config
st.set_page_config(page_title="GlowUpHub ✨", layout="centered")

# Simple girly aesthetic styling
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    h1, h2, h3 {
        color: #ff69b4;
        text-align: center;
    }
    .stButton>button {
        background-color: #ffb6c1;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 8px 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌸 GlowUpHub ✨")

# Sidebar menu
menu = st.sidebar.selectbox("💖 Menu", ["Home", "Mood", "Affirmation", "Fun"])

# ---------------- HOME ----------------
if menu == "Home":
    st.header("Welcome bestie 💕")
    st.write("🌈 Welcome to your glow-up space ✨💖")

# ---------------- MOOD ----------------
elif menu == "Mood":
    st.header("💭 Mood Check")
    mood = st.selectbox("How are you feeling? 💖", ["Happy 😊", "Sad 😢", "Tired 😴", "Frustrated 😤"])

    if mood == "Happy 😊":
        st.success("Yay! Keep shining and spreading positivity ✨💖")
    elif mood == "Sad 😢":
        st.info("It's okay to feel sad. Better days are coming 💕🌈")
    elif mood == "Tired 😴":
        st.warning("Take some rest bestie! You deserve it 🛌💖")
    elif mood == "Frustrated 😤":
        st.error("Take a deep breath. You got this 💪✨")

# ---------------- AFFIRMATION ----------------
elif menu == "Affirmation":
    st.header("🌟 Daily Motivation")

    affirmations = [
        "I am confident and strong 💖",
        "I glow differently when I take care of myself ✨",
        "I believe in my dreams 🌸",
        "I am becoming my best version 💕",
        "I deserve happiness and success 🌈"
    ]

    if st.button("Give me motivation 💫"):
        st.success(random.choice(affirmations))

# ---------------- FUN ----------------
elif menu == "Fun":
    st.header("🎀 Fun Glow-Up Tips")

    tips = [
        "💧 Drink more water",
        "🚶‍♀️ Take a short walk",
        "🔥 Stay consistent",
        "😊 Be happy",
        "🌸 Keep smiling",
        "💖 Love yourself"
    ]

    if st.button("Glow-up tip ✨"):
        st.success(random.choice(tips))

# Footer
st.markdown("---")
st.markdown("Made with 💖 using Streamlit ✨")
