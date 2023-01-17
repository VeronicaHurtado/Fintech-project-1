import pandas as pd
import streamlit as st

#setting path from csv
csv_path = ("Resources/vehicles.csv")
vehicles_df = pd.read_csv(csv_path)

# Create a drop-down menu for the year
year = st.selectbox("Select the year", vehicles_df['year'].unique())

# Create a drop-down menu for the make
make = st.selectbox("Select the make", vehicles_df['make'].unique())

# Create a drop-down menu for the model
model = st.selectbox("Select the model", vehicles_df['model'].unique())

# Create a drop-down menu for the transmission
transmission = st.selectbox("Select the transmission", vehicles_df['trany'].unique())

if st.button("Submit"):
    # Filter the data based on the user's selection
    filtered_df = vehicles_df[(vehicles_df['year'] == year) & (vehicles_df['make'] == make) & (vehicles_df['model'] == model) & (vehicles_df['trany'] == transmission)]

    # Output the fuel efficiency in litres per 100 km - Highway
    st.write("Fuel efficiency - Highway:", filtered_df['UHighway'].values[0], "L/100km")
    
    # Output the fuel efficiency in litres per 100 km - City
    st.write("Fuel efficiency - City:", filtered_df['UCity'].values[0], "L/100km")
    
    # Output the emissions in grams per kilometre
    st.write("co2 Emissions:", filtered_df['co2TailpipeGpKM'].values[0], "g/KM")

    # output the fuel type and drivetrain
    st.write("Fuel Type:", filtered_df['fuelType1'].values[0])
    st.write("Drivetrain:", filtered_df['drive'].values[0])