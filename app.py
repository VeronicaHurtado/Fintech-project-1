import streamlit as st
from streamlit_lottie import st_lottie
from functions import calculate_fuel_cost_between_destinations
from data_collection import load_lottie
from constants import ASSET_ANIMATION_ONE

# Streamlit config settings
st.set_page_config(page_title='Eco-max something', page_icon=':car::train::bicyclist:', layout='wide')
# Set page variables
animation_one = load_lottie(ASSET_ANIMATION_ONE)

# Header Section
with st.container():
    st.subheader('Sub-header text here :car::train::bicyclist:')
    st.title("Fuel Cost Calculator")
    st.write("Instructions to use this tool")
    # st.write("[This is a link example](https://streamlit.io/)")

# Form to capture the variables required for calculations
with st.container():
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

# Results (TBD)
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Your trip')
        st.write('##')
    with right_column:
        st_lottie(animation_one)
