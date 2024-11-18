import streamlit as st
import mysql.connector
from mysql.connector import Error
import pandas as pd

def show_delete_entry(db_config):
    st.title("Delete Entry")
    
    # Load Lottie animation for delete
   # st.markdown("### ⚠️ Warning: This action cannot be undone!")
    
    # Select table to delete from
    table_choice = st.selectbox(
        "Select Table",
        ["User", "SpotifyUsage", "MusicPreferences", "PodcastPreferences"]
    )
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Get existing IDs based on table selection
        if table_choice == "User":
            cursor.execute("SELECT UserID, Age, Gender FROM User")
            records = cursor.fetchall()
            columns = ["User ID", "Age", "Gender"]
        elif table_choice == "SpotifyUsage":
            cursor.execute("SELECT UsageID, UserID, UsagePeriod FROM SpotifyUsage")
            records = cursor.fetchall()
            columns = ["Usage ID", "User ID", "Usage Period"]
        elif table_choice == "MusicPreferences":
            cursor.execute("SELECT MusicID, UserID, FavoriteGenre FROM MusicPreferences")
            records = cursor.fetchall()
            columns = ["Music ID", "User ID", "Favorite Genre"]
        else:  # PodcastPreferences
            cursor.execute("SELECT PodcastID, UserID, FavoriteGenre FROM PodcastPreferences")
            records = cursor.fetchall()
            columns = ["Podcast ID", "User ID", "Favorite Genre"]
        
        # Convert records to a DataFrame and display
        df = pd.DataFrame(records, columns=columns)
        st.dataframe(df)
        
        # Delete form
        with st.form("delete_form"):
            if table_choice == "User":
                id_to_delete = st.number_input("Enter User ID to delete", min_value=1)
                id_field = "UserID"
            elif table_choice == "SpotifyUsage":
                id_to_delete = st.number_input("Enter Usage ID to delete", min_value=1)
                id_field = "UsageID"
            elif table_choice == "MusicPreferences":
                id_to_delete = st.number_input("Enter Music ID to delete", min_value=1)
                id_field = "MusicID"
            else:  # PodcastPreferences
                id_to_delete = st.number_input("Enter Podcast ID to delete", min_value=1)
                id_field = "PodcastID"
            
            submit_button = st.form_submit_button("Delete Entry")
            
            if submit_button:
                try:
                    query = f"DELETE FROM {table_choice} WHERE {id_field} = %s"
                    cursor.execute(query, (id_to_delete,))
                    conn.commit()
                    
                    if cursor.rowcount > 0:
                        st.success(f"Successfully deleted entry with ID: {id_to_delete}")
                    else:
                        st.warning(f"No entry found with ID: {id_to_delete}")
                        
                except Error as e:
                    if e.errno == 1451:  # Foreign key constraint error
                        st.error("Cannot delete this entry as it is referenced by other records.")
                    else:
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
show_delete_entry(db_config)
