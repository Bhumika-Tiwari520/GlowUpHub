import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Aura AI Dashboard",
    layout="wide"
)

st.title("💜 Aura AI Dashboard")

st.subheader("Welcome Back")

st.write("Your emotional wellness and study companion.")

# Metrics

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Mood", "84%")

with c2:
    st.metric("Focus", "78%")

with c3:
    st.metric("Study Balance", "81%")

with c4:
    st.metric("Stress", "32%")

st.divider()

# Mood Selector

mood = st.select_slider(
    "How are you feeling today?",
    options=["😢", "😟", "😐", "😊", "😁"]
)

st.success(f"Current Mood: {mood}")

st.divider()

# Quick Access

st.subheader("Quick Access")

q1, q2, q3, q4 = st.columns(4)

with q1:
    st.button("🤖 AI Chat")

with q2:
    st.button("📔 Journal")

with q3:
    st.button("🔥 Burnout")

with q4:
    st.button("📚 Study")

st.divider()

# Mood Trend Chart

data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Mood": [5, 6, 4, 7, 8, 9, 8]
})

fig = px.line(
    data,
    x="Day",
    y="Mood",
    markers=True,
    title="Weekly Mood Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info("✨ Progress is progress, no matter how small.")
