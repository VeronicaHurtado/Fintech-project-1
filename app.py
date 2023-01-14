import streamlit as st
from functions import calculate_fuel_cost_between_destinations

# Streamlit config settings
st.set_page_config(page_title='Eco-max something', page_icon=':car::train::bicyclist:', layout='wide')

# Header Section
st.subheader('Sub-header text here :car::train::bicyclist:')
st.title("Fuel Cost Calculator")
st.write("Instructions to use this tool")
# st.write("[This is a link example](https://streamlit.io/)")


# Set variables for calulations
car_make = st.text_input("Car Make:", "")
car_model = st.text_input("Car Model:", "")
# avg_speed = st.text_input("Average speed (kml):", "")
start_location = st.text_input("Start Location:", "")
end_location = st.text_input("End Location:", "")
# fuel_type = st.text_input("Fuel type:", "")
fuel_type = st.selectbox("Fuel type", ['petrol', 'diesel'])

if st.button("Calculate Fuel Cost"):
    cost = calculate_fuel_cost_between_destinations(start_location, end_location, fuel_type)
    st.success("The total fuel cost for this trip is $" + str(cost))

