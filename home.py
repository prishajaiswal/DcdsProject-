import streamlit as st
from streamlit_lottie import st_lottie
import requests


#efine function to load Lottie animations
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Add gradient background CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #4facfe, #00f2fe); /* New gradient */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Sidebar style with Spotify colors
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-image: linear-gradient(to top, #1DB954, #000000);
        color: white;
    }
    .css-1d391kg {
        color: white;
    }
    .css-184tjsw p {
        color: #1DB954;
    }
    </style>
    """, unsafe_allow_html=True) 

# Load Lottie animation URL
lottie_url = "https://lottie.host/9dbffd02-5bd7-4531-8e82-9612c8af354a/ttwtqPJ4n8.json"  # Replace with your Lottie URL
lottie_animation = load_lottie_url(lottie_url)

# Home page function
def show_home():
    st.title("Spotify Data Analysis Dashboard")
    st.header ("Welcome to Spotify Data Analysis")

    # Layout and content for the Home page with right-aligned animation
    col1, col2, col3 = st.columns([1, 1, 2])  # Adjust the width ratios as needed to align

    with col3:
        if lottie_animation is not None:
            st_lottie(lottie_animation, height=300, key="lottie_animation")
        else:
            st.warning("Failed to load animation.")
            ## Welcome to Spotify Data Analysis
    with col1:
        st.markdown("""
        ## Welcome to Spotify Data Analysis
        
        This dashboard allows you to:
        - View and analyze user preferences
        - Manage user data
        - Explore music and podcast trends
        - Generate insights from our database
        
        Get started by using the navigation menu on the left!
        """)

    # Displaying key metrics as a quick stats section
 #   st.markdown("### Quick Stats")
  #  col1, col2, col3, col4 = st.columns(4)
    
  #  with col1:
   #     st.metric("Total Users", "1,234")
   # with col2:
 #       st.metric("Active Premium Users", "789")
  #  with col3:
   #     st.metric("Most Popular Genre", "Pop")
   # with col4:
   #     st.metric("Average Age", "27")


show_home()
