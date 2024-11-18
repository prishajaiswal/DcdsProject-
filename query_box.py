import streamlit as st
import mysql.connector
from mysql.connector import Error
import pandas as pd

def show_query_box(db_config):
    st.title("Query Box")
    
    # Predefined queries
    queries = {
        "Most Popular Music Genres": """
            SELECT FavoriteGenre, COUNT(*) as Count
            FROM MusicPreferences
            GROUP BY FavoriteGenre
            ORDER BY Count DESC
        """,
        "User Age Distribution": """
            SELECT 
                CASE 
                    WHEN Age < 18 THEN 'Under 18'
                    WHEN Age BETWEEN 18 AND 24 THEN '18-24'
                    WHEN Age BETWEEN 25 AND 34 THEN '25-34'
                    WHEN Age BETWEEN 35 AND 44 THEN '35-44'
                    ELSE '45+'
                END AS AgeGroup,
                COUNT(*) as Count
            FROM User
            GROUP BY AgeGroup
            ORDER BY AgeGroup
        """,
        "Subscription Plan Distribution": """
            SELECT SubscriptionPlan, COUNT(*) as Count
            FROM SpotifyUsage
            GROUP BY SubscriptionPlan
            ORDER BY Count DESC
        """,
        "Popular Podcast Genres by Gender": """
            SELECT u.Gender, pp.FavoriteGenre, COUNT(*) as Count
            FROM User u
            JOIN PodcastPreferences pp ON u.UserID = pp.UserID
            GROUP BY u.Gender, pp.FavoriteGenre
            ORDER BY u.Gender, Count DESC
        """,
        "Listening Device Preferences": """
            SELECT ListeningDevice, COUNT(*) as Count
            FROM SpotifyUsage
            GROUP BY ListeningDevice
            ORDER BY Count DESC
        """
    }
    
    # Query selector
    selected_query = st.selectbox(
        "Select a Query",
        list(queries.keys())
    )
    
    # Display selected query
    st.code(queries[selected_query], language='sql')
    
    # Execute query button
    if st.button("Execute Query"):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            
            cursor.execute(queries[selected_query])
            results = cursor.fetchall()
            
            # Convert results to DataFrame
            df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
            
            # Display results
            st.dataframe(df)
            
            # Visualize results based on query type
            if selected_query in ["Most Popular Music Genres", "User Age Distribution", 
                                "Subscription Plan Distribution"]:
                st.bar_chart(df.set_index(df.columns[0])[df.columns[1]])
            
        except Error as e:
            st.error(f"Error executing query: {e}")
        
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()
    
    # Custom query option
    st.markdown("### Custom Query")
    custom_query = st.text_area("Enter your custom SQL query")
    
    if st.button("Execute Custom Query"):
        if custom_query:
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                
                cursor.execute(custom_query)
                results = cursor.fetchall()
                
                # Convert results to DataFrame
                df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
                
                # Display results
                st.dataframe(df)
                
            except Error as e:
                st.error(f"Error executing custom query: {e}")
            
            finally:
                if 'conn' in locals() and conn.is_connected():
                    cursor.close()
                    conn.close()
        else:
            st.warning("Please enter a query first")

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'project2'
}
(db_config)
