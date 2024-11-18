import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show_about():
    st.title("About Spotify Data Analysis")
    
    # Load Lottie animation for about page
    about_animation = load_lottie_url("https://lottie.host/f26db998-fcab-44eb-8ef9-1dfdb0eabfa9/JGtEGBdOUr.json")
    if about_animation:
        st_lottie(about_animation, speed=1, width=600, height=400, key="about_animation")

    # Create columns for the about section, which will be displayed below the image
    #col1, col2 = st.columns(2)
    
    #with col1:
    #with col1:
        st.markdown("""
        ## 🎵 About This Project
        
        The Spotify Data Analysis Dashboard is a comprehensive tool designed to analyze and manage user preferences 
        and behavior data for Spotify users. This application provides insights into music and podcast consumption 
        patterns, helping understand user preferences and trends.
        
        ### 🎯 Key Features
        
        - **User Data Management**: Add, update, and delete user information
        - **Usage Analysis**: Track how users interact with Spotify
        - **Music Preferences**: Analyze favorite genres and listening patterns
        - **Podcast Insights**: Understand podcast consumption behavior
        - **Custom Queries**: Flexible analysis options for specific insights
        
        ### 🔧 Technology Stack
        
        - **Frontend**: Streamlit
        - **Database**: MySQL
        - **Animations**: Lottie
        - **Data Analysis**: Pandas
        
        ### 📊 Data Collection
        
        Our database contains information about:
        - User demographics
        - Listening habits
        - Content preferences
        - Subscription patterns
        
        ### 🔒 Privacy & Security
        
        - All user data is anonymized
        - Secure database connections
        - Regular data backups
        - Compliance with data protection regulations
        """)

   # with col2:
       # if about_animation is not None:
        #    st_lottie(about_animation, height=300)

    # Team Section
    st.markdown("""
    ## 👥 Our Team
    
    The Spotify Data Analysis Dashboard was developed by a team of dedicated professionals:
    
    - **Data Scientists**: Analyzing patterns and creating insights
    - **Database Engineers**: Managing data structure and queries
    - **UI/UX Designers**: Creating an intuitive user experience
    - **Quality Assurance**: Ensuring reliable functionality
    
    ## 📈 Future Development
    
    We are constantly working to improve the dashboard with:
    
    1. Advanced analytics features
    2. Machine learning predictions
    3. Real-time data processing
    4. Enhanced visualization options
    5. API integration capabilities
    
    ## 📞 Contact Information
    
    For support, feedback, or inquiries:
    - 📧 Email: support@spotifyanalysis.com
    - 💬 Discord: SpotifyAnalysis
    - 📱 Twitter: @SpotifyAnalysis
    
    ## 🙏 Acknowledgments
    
    Special thanks to:
    - The Streamlit team for their amazing framework
    - Our beta testers for valuable feedback
    - The open-source community for their contributions
    """)

    # Version Information
    st.sidebar.markdown("""
    ### Version Information
    - App Version: 1.0.0
    - Last Updated: November 2024
    - Database Version: 2.1
    """)

# Call the show_about function to display the content
show_about()
