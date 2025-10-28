import streamlit as st
import datetime

st.title("👋 Hello Render App")

st.write("Welcome to your first deployed Streamlit app on Render! 🎉")

# Petite interaction
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! 👩‍💻")

# Afficher la date et l'heure
st.write("🕒 Current time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
