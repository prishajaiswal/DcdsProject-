import streamlit as st
import mysql.connector
from mysql.connector import Error

def show_update_entry(db_config):
    st.title("Update Entry")
    
    # Select table to update
    table_choice = st.selectbox(
        "Select Table",
        ["User", "SpotifyUsage", "MusicPreferences", "PodcastPreferences"]
    )
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Fetch and display existing records
        if table_choice == "User":
            cursor.execute("SELECT * FROM User")
            records = cursor.fetchall()
            st.dataframe(records)
            
            with st.form("update_user_form"):
                user_id = st.number_input("Enter User ID to update", min_value=1)
                age = st.number_input("New Age", min_value=1)
                gender = st.selectbox("New Gender", ["Male", "Female", "Other"])
                
                submit = st.form_submit_button("Update User")
                
                if submit:
                    try:
                        query = "UPDATE User SET Age = %s, Gender = %s WHERE UserID = %s"
                        cursor.execute(query, (age, gender, user_id))
                        conn.commit()
                        if cursor.rowcount > 0:
                            st.success("User updated successfully!")
                        else:
                            st.warning(f"No user found with ID: {user_id}")
                    except Error as e:
                        st.error(f"Error: {e}")
        
        elif table_choice == "SpotifyUsage":
            cursor.execute("SELECT * FROM SpotifyUsage")
            records = cursor.fetchall()
            st.dataframe(records)
            
            with st.form("update_usage_form"):
                usage_id = st.number_input("Enter Usage ID to update", min_value=1)
                user_id = st.number_input("New User ID", min_value=1)
                usage_period = st.selectbox("New Usage Period", ["Daily", "Weekly", "Monthly"])
                listening_device = st.selectbox("New Listening Device", 
                    ["Mobile", "Desktop", "Tablet", "Smart Speaker"])
                subscription_plan = st.selectbox("New Subscription Plan", 
                    ["Free", "Premium", "Family", "Student"])
                premium_willingness = st.selectbox("New Premium Willingness", 
                    ["Yes", "No", "Maybe"])
                preferred_premium_plan = st.selectbox("New Preferred Premium Plan", 
                    ["Individual", "Duo", "Family", "Student"])
                
                submit = st.form_submit_button("Update Usage Data")
                
                if submit:
                    try:
                        query = """UPDATE SpotifyUsage 
                                 SET UserID = %s, UsagePeriod = %s, ListeningDevice = %s,
                                     SubscriptionPlan = %s, PremiumWillingness = %s,
                                     PreferredPremiumPlan = %s 
                                 WHERE UsageID = %s"""
                        values = (user_id, usage_period, listening_device, subscription_plan,
                                premium_willingness, preferred_premium_plan, usage_id)
                        cursor.execute(query, values)
                        conn.commit()
                        if cursor.rowcount > 0:
                            st.success("Usage data updated successfully!")
                        else:
                            st.warning(f"No usage data found with ID: {usage_id}")
                    except Error as e:
                        st.error(f"Error: {e}")
        
        elif table_choice == "MusicPreferences":
            cursor.execute("SELECT * FROM MusicPreferences")
            records = cursor.fetchall()
            st.dataframe(records)
            
            with st.form("update_music_preferences_form"):
                music_id = st.number_input("Enter Music ID to update", min_value=1)
                user_id = st.number_input("New User ID", min_value=1)
                preferred_content = st.multiselect(
                    "New Preferred Content",
                    ["Songs", "Albums", "Playlists", "Artist Radio", "Podcasts"]
                )
                favorite_genre = st.selectbox(
                    "New Favorite Genre",
                    ["Pop", "Rock", "Hip Hop", "Jazz", "Classical", "Electronic", "R&B", "Country"]
                )
                time_slot = st.selectbox(
                    "New Time Slot",
                    ["Morning", "Afternoon", "Evening", "Night", "All Day"]
                )
                influential_mood = st.multiselect(
                    "New Influential Mood",
                    ["Happy", "Sad", "Energetic", "Relaxed", "Focused", "Party"]
                )
                listening_frequency = st.selectbox(
                    "New Listening Frequency",
                    ["Daily", "Several times a week", "Weekly", "Monthly", "Rarely"]
                )
                
                submit = st.form_submit_button("Update Music Preferences")
                
                if submit:
                    try:
                        query = """UPDATE MusicPreferences 
                                 SET UserID = %s, PreferredContent = %s, FavoriteGenre = %s,
                                     TimeSlot = %s, InfluentialMood = %s, ListeningFrequency = %s
                                 WHERE MusicID = %s"""
                        values = (user_id, ','.join(preferred_content), favorite_genre,
                                time_slot, ','.join(influential_mood), listening_frequency, music_id)
                        cursor.execute(query, values)
                        conn.commit()
                        if cursor.rowcount > 0:
                            st.success("Music preferences updated successfully!")
                        else:
                            st.warning(f"No music preferences found with ID: {music_id}")
                    except Error as e:
                        st.error(f"Error: {e}")
        
        else:  # PodcastPreferences
            cursor.execute("SELECT * FROM PodcastPreferences")
            records = cursor.fetchall()
            st.dataframe(records)
            
            with st.form("update_podcast_preferences_form"):
                podcast_id = st.number_input("Enter Podcast ID to update", min_value=1)
                user_id = st.number_input("New User ID", min_value=1)
                listening_frequency = st.selectbox(
                    "New Listening Frequency",
                    ["Daily", "Several times a week", "Weekly", "Monthly", "Rarely"]
                )
                favorite_genre = st.selectbox(
                    "New Favorite Genre",
                    ["Comedy", "News", "True Crime", "Education", "Business", "Sports", "Technology"]
                )
                preferred_format = st.selectbox(
                    "New Preferred Format",
                    ["Interview", "Solo", "Panel Discussion", "Storytelling", "Documentary"]
                )
                host_preference = st.selectbox(
                    "New Host Preference",
                    ["Single Host", "Co-hosts", "Multiple Hosts", "Guest-focused"]
                )
                
                submit = st.form_submit_button("Update Podcast Preferences")
                
                if submit:
                    try:
                        query = """UPDATE PodcastPreferences 
                                 SET UserID = %s, ListeningFrequency = %s, FavoriteGenre = %s,
                                     PreferredFormat = %s, HostPreference = %s
                                 WHERE PodcastID = %s"""
                        values = (user_id, listening_frequency, favorite_genre,
                                preferred_format, host_preference, podcast_id)
                        cursor.execute(query, values)
                        conn.commit()
                        if cursor.rowcount > 0:
                            st.success("Podcast preferences updated successfully!")
                        else:
                            st.warning(f"No podcast preferences found with ID: {podcast_id}")
                    except Error as e:
                        st.error(f"Error: {e}")
    
    except Error as e:
        st.error(f"Error connecting to database: {e}")
    
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'project2'
}
show_update_entry(db_config)


