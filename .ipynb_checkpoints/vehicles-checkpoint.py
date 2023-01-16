import pandas as pd
import streamlit as st

st.title("Vehicle Information")

#setting path from csv
csv_path = ("Resources/vehicles.csv")
vehicles_df = pd.read_csv(csv_path)

# Create a drop-down menu for sorting by
sort_by = st.selectbox("Sort by", ['year', 'make', 'model', 'trany', 'UHighway', 'fuelType', 'Drivetrain'])

# Create a checkbox for ascending/descending order
sort_order = st.checkbox("Sort in ascending order", value=True)

# Create a drop-down menu for filtering by
filter_by = st.selectbox("Filter by", ['year', 'make', 'model', 'trany', 'UHighway', 'fuelType', 'Drivetrain'])

# Create a text input for filter value
filter_value = st.text_input("Enter filter value")

if st.button("Submit"):
    # Filter the data based on the user's input
    filtered_df = df[df[filter_by] == filter_value]

    # Sort the data based on the user's input
    sorted_df = filtered_df.sort_values(by=sort_by, ascending=sort_order)

    # Output the sorted and filtered data
    st.write(sorted_df)