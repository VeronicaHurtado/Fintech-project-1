import streamlit as st
from streamlit_lottie import st_lottie
from functions import calculate_trip_fuel_cost
from data_collection import load_lottie, load_vehicles_df, get_distance, get_directions
from constants import ASSET_ANIMATION_ONE

# Streamlit config settings
st.set_page_config(page_title='Eco-max something', page_icon=':car:', layout='wide')
# Set page variables
animation_one = load_lottie(ASSET_ANIMATION_ONE)
petrol_trip_cost = 0.00
# Load vehicles data to Pandas Dataframe
vehicles_df = load_vehicles_df()

# Header Section
with st.container():
    st.subheader('EcoMaxi :car: :train: :bicyclist:')
    st.title("Fuel Cost Calculator")
    st.write("Instructions to use this tool")

# Form to capture the variables required for calculations
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        # Create a drop-down menu for the year
        year = st.selectbox("Select the year", vehicles_df['year'].unique())
        # Create a drop-down menu for the make
        make = st.selectbox("Select the make", vehicles_df[vehicles_df['year'] == year]['make'].unique())
        # Create a drop-down menu for the model
        model = st.selectbox("Select the model",
                             vehicles_df[(vehicles_df['year'] == year) & (vehicles_df['make'] == make)][
                                 'model'].unique())
        # Create a drop-down menu for the transmission
        transmission = st.selectbox("Select the transmission", vehicles_df[
            (vehicles_df['year'] == year) & (vehicles_df['make'] == make) & (vehicles_df['model'] == model)][
            'trany'].unique())
        # Start address
        start_location = st.text_input("Start Location:", "")
        # Destination address
        end_location = st.text_input("End Location:", "")
        # Fuel type = st.text_input("Fuel type:", "")
        fuel_type = st.selectbox("Fuel type", ['petrol', 'diesel'])

        if st.button("Submit"):
            # Filter the data based on the user's selection
            filtered_df = vehicles_df[
                (vehicles_df['year'] == year) & (vehicles_df['make'] == make) & (vehicles_df['model'] == model) & (
                            vehicles_df['trany'] == transmission)]
            # Get distance in Kilometres between given locations
            distance = get_distance(origins=start_location, destinations=end_location)
            # Get fuel cost by distance and fuel type
            petrol_trip_cost = calculate_trip_fuel_cost(fuel_type, distance)
            # Get Public Transport details
            public_transport = get_directions(origin=start_location, destination=end_location, mode='transit')

            if distance <= 25:  # If distance is less or equal than 25 Kilometres
                # Also calculate alternative modes
                bicycling = get_directions(origin=start_location, destination=end_location, mode='bicycling')
                walking = get_directions(origin=start_location, destination=end_location, mode='walking')

    with right_column:
        st_lottie(animation_one)

# Results
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Your trip')
        st.write('##')
        if petrol_trip_cost > 0:
            st.write("The total fuel cost for this trip is $" + str(petrol_trip_cost))

            # Output the fuel efficiency in litres per 100 km - Highway
            st.write("Fuel efficiency - Highway:", filtered_df['UHighway'].values[0], "L/100km")

            # Output the fuel efficiency in litres per 100 km - City
            st.write("Fuel efficiency - City:", filtered_df['UCity'].values[0], "L/100km")

            # Output the emissions in grams per kilometre
            st.write("co2 Emissions:", filtered_df['co2TailpipeGpKM'].values[0], "g/KM")

            # output the fuel type and drivetrain
            st.write("Fuel Type:", filtered_df['fuelType1'].values[0])
            st.write("Drivetrain:", filtered_df['drive'].values[0])
    with right_column:
        st.write('#Plots here?#')
