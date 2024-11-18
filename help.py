import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show_help():
    st.title("Help Guide")
    
    # Load Lottie animation for help page
    lottie_help = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_qr6xnihu.json")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        # How to Use This Application
        
        Welcome to the Spotify Data Analysis Dashboard! This guide will help you navigate through the various features of our application.
        
        ## 📌 Navigation
        - Use the sidebar menu to switch between different pages
        - Each page has specific functionality for managing and analyzing Spotify user data
        
        ## 📝 Data Management Pages
        
        ### 1. Add Entry
        - Select the table you want to add data to
        - Fill in all required fields
        - Click 'Submit' to add the entry
        - Note: UserID must exist before adding related entries
        
        ### 2. Update Entry
        - Choose the table to update
        - Enter the ID of the record you want to modify
        - Update the desired fields
        - Click 'Update' to save changes
        
        ### 3. Delete Entry
        - Select the table
        - Enter the ID of the record to delete
        - Confirm deletion
        - Note: Cannot delete records referenced by other tables
        
        ## 📊 Analysis Features
        
        ### Query Box
        - Choose from predefined queries using the dropdown
        - View SQL query before execution
        - Execute query to see results
        - Use custom query option for specific analysis
        
        ## 💡 Tips
        1. Always verify IDs before updating or deleting
        2. Use the dataframe displays to check existing records
        3. Check error messages for troubleshooting
        4. Back up important data before deletion
        
        ## ⚠️ Common Issues
        1. Foreign Key Constraints
           - Ensure referenced records exist
           - Delete dependent records first
        
        2. Invalid Data
           - Check data types match requirements
           - Verify required fields are filled
        
        3. Connection Issues
           - Verify database connectivity
           - Check credentials if needed
        """)
    
    with col2:
        if lottie_help is not None:
            st_lottie(lottie_help, height=300)
        
        st.markdown("""
        ## 🔍 Quick Links
        - [Database Schema](#database-schema)
        - [Query Examples](#query-examples)
        - [Troubleshooting](#common-issues)
        """)
    
    # Database Schema Section
    st.markdown("""
    ## Database Schema
    
    ### User Table
    ```sql
    UserID (Primary Key)
    Age
    Gender
    ```
    
    ### SpotifyUsage Table
    ```sql
    UsageID (Primary Key)
    UserID (Foreign Key)
    UsagePeriod
    ListeningDevice
    SubscriptionPlan
    PremiumWillingness
    PreferredPremiumPlan
    ```
    
    ### MusicPreferences Table
    ```sql
    MusicID (Primary Key)
    UserID (Foreign Key)
    PreferredContent
    FavoriteGenre
    TimeSlot
    InfluentialMood
    ListeningFrequency
    ExplorationMethod
    RecommendationRating
    ```
    
    ### PodcastPreferences Table
    ```sql
    PodcastID (Primary Key)
    UserID (Foreign Key)
    ListeningFrequency
    FavoriteGenre
    PreferredFormat
    HostPreference
    PreferredDuration
    VarietySatisfaction
    ```
    """)

    # Need Help Section
    st.markdown("""
    ## 📞 Need More Help?
    
    If you need additional assistance:
    1. Check the error messages for specific issues
    2. Review the database schema for proper relationships
    3. Contact the system administrator for database access issues
    4. Report bugs or suggest improvements through the feedback form
    """)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'project2'
}
show_help()

#show_help(db_config)
