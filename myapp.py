import streamlit as st

st.set_page_config(
    page_title="Aura AI",
    page_icon="💜",
    layout="wide"
)

st.title("💜 Aura AI")

st.subheader("Your Safe Space. Your Growth Partner.")

st.write("Welcome to Aura AI!")

if st.button("Get Started"):
    st.success("Aura AI is running successfully!")
