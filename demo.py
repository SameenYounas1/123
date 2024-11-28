import streamlit as st

# Title
st.title("Hello, World!")

# Subtitle
st.subheader("Welcome to your first Streamlit app!")

# Display text
st.write("This is a simple example of a Streamlit app. 🎉")

# Button interaction
if st.button("Click me"):
    st.write("Hello, Streamlit user! 👋")
else:
    st.write("Click the button to see a message!")
