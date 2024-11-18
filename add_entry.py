import streamlit as st
import mysql.connector
from mysql.connector import Error

def show_add_entry(db_config):
    st.title("Add New Entry")
    
    # Select table to add entry
    table_choice = st.selectbox(
        "Select Table",
        ["User", "SpotifyUsage", "MusicPreferences", "PodcastPreferences"]
    )
    
    if table_choice == "User":
        with st.form("add_user_form"):
            user_id = st.number_input("User ID", min_value=1)
            age = st.number_input("Age", min_value=1)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            
            submit_button = st.form_submit_button("Add User")
            
            if submit_button:
                try:
                    conn = mysql.connector.connect(**db_config)
                    cursor = conn.cursor()
                    
                    query = "INSERT INTO User (UserID, Age, Gender) VALUES (%s, %s, %s)"
                    cursor.execute(query, (user_id, age, gender))
                    
                    conn.commit()
                    st.success("User added successfully!")
                    
                except Error as e:
                    st.error(f"Error: {e}")
                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()
    
    elif table_choice == "SpotifyUsage":
        with st.form("add_usage_form"):
            usage_id = st.number_input("Usage ID", min_value=1)
            user_id = st.number_input("User ID", min_value=1)
            usage_period = st.selectbox("Usage Period", ["Daily", "Weekly", "Monthly"])
            listening_device = st.selectbox("Listening Device", ["Mobile", "Desktop", "Tablet", "Smart Speaker"])
            subscription_plan = st.selectbox("Subscription Plan", ["Free", "Premium", "Family", "Student"])
            premium_willingness = st.selectbox("Premium Willingness", ["Yes", "No", "Maybe"])
            preferred_premium_plan = st.selectbox("Preferred Premium Plan", ["Individual", "Duo", "Family", "Student"])
            
            submit_button = st.form_submit_button("Add Usage Data")
            
            if submit_button:
                try:
                    conn = mysql.connector.connect(**db_config)
                    cursor = conn.cursor()
                    
                    query = """INSERT INTO SpotifyUsage 
                             (UsageID, UserID, UsagePeriod, ListeningDevice, SubscriptionPlan, 
                              PremiumWillingness, PreferredPremiumPlan) 
                             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                    values = (usage_id, user_id, usage_period, listening_device, subscription_plan,
                            premium_willingness, preferred_premium_plan)
                    
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Usage data added successfully!")
                    
                except Error as e:
                    st.error(f"Error: {e}")
                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()

    # Similar forms for MusicPreferences and PodcastPreferences...
    # (I'll provide these in the next parts due to length constraints)
    
    elif table_choice == "MusicPreferences":
        with st.form("add_music_preferences_form"):
            music_id = st.number_input("Music ID", min_value=1)
            user_id = st.number_input("User ID", min_value=1)
            preferred_content = st.multiselect(
                "Preferred Content",
                ["Songs", "Albums", "Playlists", "Artist Radio", "Podcasts"]
            )
            favorite_genre = st.selectbox(
                "Favorite Genre",
                ["Pop", "Rock", "Hip Hop", "Jazz", "Classical", "Electronic", "R&B", "Country"]
            )
            time_slot = st.selectbox(
                "Preferred Time Slot",
                ["Morning", "Afternoon", "Evening", "Night", "All Day"]
            )
            influential_mood = st.multiselect(
                "Influential Mood",
                ["Happy", "Sad", "Energetic", "Relaxed", "Focused", "Party"]
            )
            listening_frequency = st.selectbox(
                "Listening Frequency",
                ["Daily", "Several times a week", "Weekly", "Monthly", "Rarely"]
            )
            exploration_method = st.multiselect(
                "Exploration Method",
                ["Recommendations", "Charts", "Friends", "Social Media", "Random Discovery"]
            )
            recommendation_rating = st.slider(
                "Recommendation Rating",
                1, 10, 5
            )
            
            submit_button = st.form_submit_button("Add Music Preferences")
            
            if submit_button:
                try:
                    conn = mysql.connector.connect(**db_config)
                    cursor = conn.cursor()
                    
                    query = """INSERT INTO MusicPreferences 
                             (MusicID, UserID, PreferredContent, FavoriteGenre, TimeSlot,
                              InfluentialMood, ListeningFrequency, ExplorationMethod, RecommendationRating) 
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    values = (music_id, user_id, ','.join(preferred_content), favorite_genre,
                            time_slot, ','.join(influential_mood), listening_frequency,
                            ','.join(exploration_method), str(recommendation_rating))
                    
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Music preferences added successfully!")
                    
                except Error as e:
                    st.error(f"Error: {e}")
                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()
    
    elif table_choice == "PodcastPreferences":
        with st.form("add_podcast_preferences_form"):
            podcast_id = st.number_input("Podcast ID", min_value=1)
            user_id = st.number_input("User ID", min_value=1)
            listening_frequency = st.selectbox(
                "Listening Frequency",
                ["Daily", "Several times a week", "Weekly", "Monthly", "Rarely"]
            )
            favorite_genre = st.selectbox(
                "Favorite Genre",
                ["Comedy", "News", "True Crime", "Education", "Business", "Sports", "Technology"]
            )
            preferred_format = st.selectbox(
                "Preferred Format",
                ["Interview", "Solo", "Panel Discussion", "Storytelling", "Documentary"]
            )
            host_preference = st.selectbox(
                "Host Preference",
                ["Single Host", "Co-hosts", "Multiple Hosts", "Guest-focused"]
            )
            preferred_duration = st.selectbox(
                "Preferred Duration",
                ["Under 30 mins", "30-60 mins", "1-2 hours", "Over 2 hours"]
            )
            variety_satisfaction = st.selectbox(
                "Variety Satisfaction",
                ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]
            )
            
            submit_button = st.form_submit_button("Add Podcast Preferences")
            
            if submit_button:
                try:
                    conn = mysql.connector.connect(**db_config)
                    cursor = conn.cursor()
                    
                    query = """INSERT INTO PodcastPreferences 
                             (PodcastID, UserID, ListeningFrequency, FavoriteGenre,
                              PreferredFormat, HostPreference, PreferredDuration, VarietySatisfaction) 
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                    values = (podcast_id, user_id, listening_frequency, favorite_genre,
                            preferred_format, host_preference, preferred_duration,
                            variety_satisfaction)
                    
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Podcast preferences added successfully!")
                    
                except Error as e:
                    st.error(f"Error: {e}")
                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'project2'
}
show_add_entry(db_config)
