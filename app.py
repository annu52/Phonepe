import streamlit as st
from map import show_map
from analysis import show_analysis

# Sidebar Navigation
st.sidebar.title("📊 Navigation")

page = st.sidebar.selectbox(
    "Go to",
    ["Home", "Analysis"]
)

# Routing
if page == "Home":
    show_map()

elif page == "Analysis":
    show_analysis()