import streamlit as slt
slt.set_page_config(layout="wide")  # This must be the first Streamlit command

import pandas as pd
from streamlit_option_menu import option_menu
from datetime import datetime

# Load bus route lists from CSV files
def load_route_lists():
    df_AP = pd.read_csv(r"C:/streamlit_day2/myappr/AP_data.csv")
    df_TS = pd.read_csv(r"C:/streamlit_day2/myappr/tsrtc_data2.csv")
    df_KL = pd.read_csv(r"C:/streamlit_day2/myappr/ksrtc_data3.csv")
    df_RS = pd.read_csv(r"C:/streamlit_day2/myappr/rsrtc_data4.csv")
    df_HR = pd.read_csv(r"C:/streamlit_day2/myappr/hrtc_data5.csv")
    df_CTU = pd.read_csv(r"C:/streamlit_day2/myappr/ctu_data6.csv")
    df_SB = pd.read_csv(r"C:/streamlit_day2/myappr/sbstc_data6.csv")
    df_UP = pd.read_csv(r"C:/streamlit_day2/myappr/upsrtc_data.csv")
    df_PE = pd.read_csv(r"C:/streamlit_day2/myappr/pepsu_data.csv")
    df_WB = pd.read_csv(r"C:/streamlit_day2/myappr/wbtc_data.csv")
    df_BS = pd.read_csv(r"C:/streamlit_day2/myappr/bsrtc_data01.csv")
    df_AS = pd.read_csv(r"C:/streamlit_day2/myappr/astc_data.csv")

    lists_AP = df_AP["Route_name"].tolist()
    lists_TS = df_TS["Route_name"].tolist()
    lists_KL = df_KL["Route_name"].tolist()
    lists_RS = df_RS["Route_name"].tolist()
    lists_HR = df_HR["Route_name"].tolist()
    lists_CTU = df_CTU["Route_name"].tolist()
    lists_SB = df_SB["Route_name"].tolist()
    lists_UP = df_UP["Route_name"].tolist()
    lists_PE = df_PE["Route_name"].tolist()
    lists_WB = df_WB["Route_name"].tolist()
    lists_BS = df_BS["Route_name"].tolist()
    lists_AS = df_AS["Route_name"].tolist()

    return lists_AP, lists_TS, lists_KL, lists_RS, lists_HR, lists_CTU, lists_SB, lists_UP, lists_PE, lists_WB, lists_BS, lists_AS

# Load route lists and data
lists_AP, lists_TS, lists_KL, lists_RS, lists_HR, lists_CTU, lists_SB, lists_UP, lists_PE, lists_WB, lists_BS, lists_AS = load_route_lists()

# Define get_routes function outside of page-specific logic so it can be reused across pages
def get_routes(state):
    if state == "Andhra Pradesh":
        return lists_AP
    elif state == "Telangana":
        return lists_TS
    elif state == "Kerala":
        return lists_KL
    elif state == "Rajasthan":
        return lists_RS
    elif state == "Himachal":
        return lists_HR
    elif state == "Chandigarh":
        return lists_CTU
    elif state == "South Bengal":
        return lists_SB
    elif state == "Uttar Pradesh":
        return lists_UP
    elif state == "Punjab":
        return lists_PE
    elif state == "West Bengal":
        return lists_WB
    elif state == "Bihar":
        return lists_BS
    elif state == "Assam":
        return lists_AS

# Load CSV file into a DataFrame
def load_csv_data():
    try:
        return pd.read_csv(r"C:/streamlit_day2/myappr/redbusdata12.csv")
    except Exception as e:
        slt.error(f"Error loading data: {e}")
        return pd.DataFrame()

df_redbus = load_csv_data()

# Convert Price column to numeric, coerce errors to NaN
df_redbus['Price'] = pd.to_numeric(df_redbus['Price'], errors='coerce')

# Remove rows with NaN values in Price
df_redbus = df_redbus.dropna(subset=['Price'])

# Navigation menu
web = option_menu(menu_title="Welcome to Redbus",
                  options=["Home", "About us", "Bus details", "Bus Booking", "Terms and Conditions", "FAQ"],  # Add "FAQ"
                  icons=["house", "info-circle", "bus", "ticket", "file-text", "question-circle"],  # Added relevant icon
                  orientation="horizontal")

# Home page
if web == "Home":
    slt.image("C:/Users/Shalini/Downloads/WhatsApp Image 2024-09-26 at 8.40.12 PM.jpeg", width=200)
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":blue[Domain:] Transportation")
    slt.image("C:/Users/Shalini/Downloads/WhatsApp Image 2024-09-26 at 8.43.07 PM.jpeg", width=400)
    slt.subheader(":blue[Objective:]")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data.")
    slt.subheader(":blue[Overview:]")
    slt.markdown('''Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites.
                    Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    MySQL: The extracted data is stored in MySQL for further querying and filtering.
                    Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.''')

# About us page
if web == "About us":
    slt.title("About Us")
    slt.subheader("Welcome to Redbus Data Scraping and Filtering Application")
    slt.markdown(
        """
        **Objective**: 
        Our primary goal is to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. This application allows users to easily filter and find relevant bus travel information across various states in India.

        **What We Do**:
        - We scrape data from multiple state-run bus services to provide a centralized platform for bus route and fare information.
        - Users can filter bus details based on criteria like bus type, fare range, and time of travel, making it easier to plan their journeys.
        
        **Technologies Used**:
        - **Selenium**: A powerful tool for web scraping, allowing us to automate the extraction of data from websites.
        - **Pandas**: A robust library for data manipulation and analysis, enabling us to handle large datasets efficiently.
        - **MySQL**: Used for storing the scraped data for further querying and analysis.
        - **Streamlit**: A user-friendly framework that facilitates the creation of interactive web applications for data visualization.

        **Our Vision**:
        We aim to provide an intuitive and efficient platform for travelers to access bus travel information, thus enhancing their travel planning experience. 

        **Developed By**: Shalini Raju
        """
    )

# Bus details page
if web == "Bus details":
    S = slt.selectbox("Lists of States", ["Andhra Pradesh", "Telangana", "Kerala", "Rajasthan", "Himachal", "Chandigarh",
                                          "South Bengal", "Uttar Pradesh", "Punjab", "West Bengal", "Bihar", "Assam"])

    col1, col2 = slt.columns(2)
    with col1:
        select_type = slt.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))

    TIME = slt.time_input("Select the time")

    # Route-specific filtering logic
    route = slt.selectbox("List of routes", get_routes(S))

    # Add a submit button
    if slt.button("Submit"):
        def query_bus_details(route_name, bus_type, fare_range, time_value):
            # Define fare range
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # High max for "2000 and above"

            # Define bus type condition
            bus_type_condition = {
                "sleeper": "Sleeper",
                "semi-sleeper": "Semi Sleeper",
                "others": "Other"
            }.get(bus_type, "")

            # Convert selected time to comparable format
            dummy_date = datetime.today().date()  # Use today's date
            combined_time = datetime.combine(dummy_date, time_value)

            # Filter CSV data based on user input
            filtered_data = df_redbus[
                (df_redbus['Price'].between(fare_min, fare_max)) &
                (df_redbus['Route_name'] == route_name) &
                (df_redbus['Bus_type'].str.contains(bus_type_condition, na=False)) &  # added na=False
                (pd.to_datetime(df_redbus['Start_time'], errors='coerce') >= combined_time)
            ]

            return filtered_data

        # Query and display results
        df_result = query_bus_details(route, select_type, select_fare, TIME)
        slt.dataframe(df_result)
    

import csv
from datetime import datetime

# Bus Booking page
if web == "Bus Booking":
    slt.title("Bus Booking")
    slt.subheader("Select your travel details:")
    
    state = slt.selectbox("Choose State", ["Andhra Pradesh", "Telangana", "Kerala", "Rajasthan", "Himachal", "Chandigarh", "South Bengal", "Uttar Pradesh", "Punjab", "West Bengal", "Bihar", "Assam"])
    route_booking = slt.selectbox("Choose Route", get_routes(state))
    booking_date = slt.date_input("Select the travel date")
    num_passengers = slt.number_input("Number of Passengers", min_value=1, max_value=10)
    
    # Fetch the price for the selected route
    selected_bus = df_redbus[df_redbus['Route_name'] == route_booking]
    selected_bus_price = selected_bus['Price'].mean()
    
    if 'Rating' in selected_bus.columns:
        selected_bus_rating = selected_bus['Rating'].mean()
    else:
        selected_bus_rating = None

    # Allow users to add their own rating
    user_rating = slt.slider("Rate this Bus", min_value=1, max_value=5, step=1)
    
    total_price = selected_bus_price * num_passengers

    # Display booking summary and user rating
    slt.subheader("Booking Summary")
    slt.markdown(f"**State**: {state}")
    slt.markdown(f"**Route**: {route_booking}")
    slt.markdown(f"**Travel Date**: {booking_date}")
    slt.markdown(f"**Number of Passengers**: {num_passengers}")
    slt.markdown(f"**Ticket Price (per passenger)**: ₹{selected_bus_price:.2f}")
    slt.markdown(f"**Total Price**: ₹{total_price:.2f}")
    
    if selected_bus_rating is not None:
        slt.markdown(f"**Average Bus Rating**: {selected_bus_rating:.1f} / 5.0")
    else:
        slt.markdown("**Average Bus Rating**: N/A")
    
    slt.markdown(f"**Your Rating for this Bus**: {user_rating} / 5.0")
    
    if slt.button("Done"):
        # Save the rating to the CSV file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Open the file and append the rating
        with open('ratings_file', 'a', newline='') as f:
            writer = csv.writer(f)  # Correct usage of csv.writer
            writer.writerow([route_booking, user_rating, timestamp])
        
        slt.success(f"Rating of {user_rating} for the route '{route_booking}' Booking  Successfully Done!")




# Terms and Conditions page
if web == "Terms and Conditions":
    slt.title("Terms and Conditions")
    slt.subheader("Please read the following terms and conditions carefully:")
    slt.markdown(
        """
        1. **Accuracy of Information**: The data provided in this application is collected from various bus operators and may not always be up-to-date. While we strive to ensure the accuracy of the information, we cannot guarantee that all details are correct at all times.
        
        2. **Use of Application**: The application is intended for personal use only. Unauthorized commercial use of this application is strictly prohibited.
        
        3. **Booking Responsibility**: The user is solely responsible for any bookings made through third-party payment gateways. We are not liable for any issues that arise during or after the booking process.
        
        4. **Privacy Policy**: The data collected from users will not be shared with third parties without explicit consent. However, anonymized usage statistics may be collected for improving the service.
        
        5. **Modification of Terms**: We reserve the right to modify these terms and conditions at any time without prior notice. It is the user's responsibility to stay updated with the latest version of the terms.
        
        6. **Limitation of Liability**: We are not responsible for any losses or damages arising from the use of this application, including but not limited to direct, indirect, incidental, punitive, and consequential damages.
        
        7. **Governing Law**: These terms and conditions are governed by and construed in accordance with the laws of India. Any disputes arising in connection with these terms shall be subject to the exclusive jurisdiction of the courts in India.
        
        By using this application, you agree to these terms and conditions.
        """
    )

# FAQ page
if web == "FAQ":
    slt.title("Frequently Asked Questions")
    slt.subheader("Find answers to common questions below:")
    slt.markdown(
        """
        1. **What is Redbus Data Scraping with Selenium & Streamlit?**  
        This is a project that automates the extraction of bus route data from Redbus and provides a user-friendly interface for filtering and exploring the data.

        2. **What states are supported?**  
        The application currently supports bus routes from Andhra Pradesh, Telangana, Kerala, Rajasthan, Himachal Pradesh, Chandigarh, South Bengal, Uttar Pradesh, Punjab, West Bengal, Bihar, and Assam.

        3. **How is the data collected?**  
        Data is scraped from the Redbus website using Selenium, which automates the extraction of relevant bus details and routes.

        4. **Can I book a bus through this app?**  
        No, this app does not facilitate direct bus bookings. It provides information that helps users find buses and plan their journeys, but booking must be done through other platforms.

        5. **How can I filter bus data?**  
        You can filter data based on bus type, fare range, availability of seats, and travel timings using the app’s built-in filters.

        6. **Is the data updated in real-time?**  
        No, the data is not updated in real-time. It is periodically refreshed through web scraping, so there may be some delay between updates.

        7. **Who developed this application?**  
        The application was developed by Shalini Raju as part of a project focusing on data scraping and visualization.
        """
    )

