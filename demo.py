import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu  
# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='redbusdata'
)

if mydb.is_connected():
    st.markdown(f"## <span style='color:white'>RedBus Project </span>", unsafe_allow_html=True)

mycursor = mydb.cursor(buffered=True)


st.markdown(
    """
    <style>
    .stApp {
        background-color:#333333; /* Light black */
    }
    label[data-testid="stSelectLabel"] {
        color: white !important;
    }
    label[data-testid="stTextInputLabel"] {
        color: white !important;
    }
    .css-1d391kg p {
        color: white !important; /* Text inside markdown elements */
    }
    .css-16huue1.e16nr0p34 {
        color: white !important; /* Slider label text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    selected_page = option_menu(
        "Main Menu",
        ["Home", "Bus Filter Form"],
        icons=['house', 'filter'],
        menu_icon="cast",
        default_index=0,
    )

if selected_page == "Home":
    st.image(r"C:\Users\DELL\Desktop\Logo\rdc-redbus-logo.png", width=100)  
    st.markdown("<h1 style='color:white;'>Welcome to the RedBus Project</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color:white;'>
    The RedBus project is designed to help users search for bus services between different cities and filter buses based on
    criteria like rating, departure time, and more. This platform integrates with a MySQL database to retrieve real-time 
    bus information and provide users with accurate and updated details.
    </p>
    <h2 style='color:white;'>How the App Works:</h2>
    <ul style='color:white;'>
        <li><strong>Search Buses:</strong> Enter your departure and destination cities to search for available bus routes.</li>
        <li><strong>Filter by Rating:</strong> Use the slider to filter buses based on their ratings.</li>
        <li><strong>Filter by Time:</strong> Filter buses that depart after a specific time of day.</li>
        <li><strong>Filter by Price:</strong> Use the slider to select a range of ticket prices.</li>
    </ul>
    <p style='color:white;'>Navigate to the "Bus Filter Form" from the sidebar to get started.</p>
    """, unsafe_allow_html=True)

if selected_page == "Bus Filter Form":

    mycursor.execute("SELECT DISTINCT StateName FROM final_bus_details")
    states = [state[0] for state in mycursor.fetchall()]

    mycursor.execute("SELECT DISTINCT From_Place FROM final_bus_details")
    from_places = [place[0] for place in mycursor.fetchall()]

    mycursor.execute("SELECT DISTINCT To_Place FROM final_bus_details")
    to_places = [place[0] for place in mycursor.fetchall()]

    with st.form("bus_filter_form"):
        st.image(r"C:\Users\DELL\Desktop\Logo\rdc-redbus-logo.png", width=100)  
        st.markdown(f"## <span style='color:white'>Bus Filter Form</span>", unsafe_allow_html=True)
        
        selected_state = st.selectbox("Select State", states)

        selected_from_place = st.selectbox("Select Departure Place", from_places)
        
        selected_to_place = st.selectbox("Select Destination Place", to_places)
        
        selected_rating = st.slider('Select Minimum Bus Rating', min_value=0.0, max_value=5.0, value=3.0, step=0.1)
        
        time_filter = st.slider("Select Time (HH:MM) for Departure Filter (After selected time)", 
                                min_value=0, max_value=23, value=18, step=1)
        
        
        min_price, max_price = st.slider('Select Ticket Price Range', min_value=100, max_value=5000, value=(300, 2000), step=100)

        
        submit_button = st.form_submit_button(label='Submit')

    
    if submit_button:
        selected_time = f"{time_filter:02d}:00:00"

        
        st.write("Debugging Info:")
        st.write(f"State: {selected_state}")
        st.write(f"From Place: {selected_from_place}")
        st.write(f"To Place: {selected_to_place}")
        st.write(f"Rating: {selected_rating}")
        st.write(f"Time: {selected_time}")
        st.write(f"Price Range: {min_price} - {max_price}")

        
        query = f"""
            SELECT BusName, BusType, BusDepartureTime, BusReachingTime, TicketPrice, BusRating
            FROM final_bus_details 
            WHERE LOWER(StateName) = LOWER('{selected_state}')
            AND LOWER(From_Place) = LOWER('{selected_from_place}') 
            AND LOWER(To_Place) = LOWER('{selected_to_place}') 
            AND BusRating >= {selected_rating} 
            AND STR_TO_DATE(BusDepartureTime, '%H:%i:%s') > '{selected_time}'
            AND CAST(REPLACE(TicketPrice, 'INR ', '') AS DECIMAL(10,2)) BETWEEN {min_price} AND {max_price}
        """

        
        st.write(f"Executed Query: {query}")

        try:
            mycursor.execute(query)

            
            filtered_data = mycursor.fetchall()

            if filtered_data:
                df = pd.DataFrame(filtered_data, columns=['BusName', 'BusType', 'BusDepartureTime', 'BusReachingTime', 'TicketPrice', 'BusRating'])
                st.markdown(f"### <span style='color:white'>Filtered Bus Details for {selected_from_place} to {selected_to_place}</span>", unsafe_allow_html=True)
                st.write(df)
            else:
                st.write("No buses found with the selected filters.")
        
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
