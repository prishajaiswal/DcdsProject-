import streamlit as st
import requests
import mysql.connector
from mysql.connector import Error
import json

# Set the page configuration
st.set_page_config(page_title="Spotify Data Analysis", layout="wide") 
# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'project2'
}

# Define function to load lottie animations
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Page Setup ---
home_page = st.Page(
    page="./home.py",
    title="🏠 Home - Spotify Data Analysis",
    default=True
)

add_entry_page = st.Page(
    page="./add_entry.py",
    title="➕ Add Entry"
)

delete_entry_page = st.Page(
    page="./delete_entry.py",
    title="🗑️ Delete Entry"
)

update_entry_page = st.Page(
    page="./update_entry.py",
    title="✏️ Update Entry"
)

query_box_page = st.Page(
    page="./query_box.py",
    title="🔍 Query Box"
)

help_page = st.Page(
    page="./help.py",
    title="❓ Help"
)

about_page = st.Page(
    page="./about.py",
    title="ℹ️ About"
)

# --- Navigation ---
pg = st.navigation({
    "Main Features": [home_page, add_entry_page, delete_entry_page, update_entry_page],
    "Utilities": [help_page, about_page]
})

# Run the selected page
pg.run()
