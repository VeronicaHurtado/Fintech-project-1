{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "87f27ff2-c8dc-423b-a28b-986348c05457",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "aec71b12-75c4-498f-8da9-90a79d5b0290",
   "metadata": {},
   "outputs": [],
   "source": [
    "#setting path from csv\n",
    "csv_path = (\"Resources/vehicles.csv\")\n",
    "vehicles_df = pd.read_csv(csv_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "de5629a5-d51c-4045-af0d-0691bc535b8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sort the data by make, model, year, and transmission\n",
    "vehicles_df.sort_values(by=['make', 'model', 'year', 'trany'], inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "67d97046-ee98-4fc4-a2f8-80d36239ef69",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a drop-down menu for the year\n",
    "year = st.selectbox(\"Select the year\", vehicles_df['year'].unique())\n",
    "\n",
    "# Create a drop-down menu for the make\n",
    "make = st.selectbox(\"Select the make\", vehicles_df['make'].unique())\n",
    "\n",
    "# Create a drop-down menu for the model\n",
    "model = st.selectbox(\"Select the model\", vehicles_df['model'].unique())\n",
    "\n",
    "# Create a drop-down menu for the transmission\n",
    "transmission = st.selectbox(\"Select the transmission\", vehicles_df['trany'].unique())\n",
    "\n",
    "if st.button(\"Submit\"):\n",
    "    # Filter the data based on the user's selection\n",
    "    filtered_df = vehicles_df[(vehicles_df['year'] == year) & (vehicles_df['make'] == make) & (vehicles_df['model'] == model) & (vehicles_df['trany'] == transmission)]\n",
    "\n",
    "    # Output the fuel efficiency in litres per 100 km - Highway\n",
    "    st.write(\"Fuel efficiency:\", filtered_df['UHighway'].values[0], \"L/100km\")\n",
    "    \n",
    "    # Output the fuel efficiency in litres per 100 km - City\n",
    "    st.write(\"Fuel efficiency:\", filtered_df['UCity'].values[0], \"L/100km\")\n",
    "\n",
    "    # output the fuel type and drivetrain\n",
    "    st.write(\"Fuel Type:\", filtered_df['FuelType'].values[0])\n",
    "    st.write(\"Drivetrain:\", filtered_df['Drivetrain'].values[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ad2ec284-c024-42d8-bbda-a18ad41ae262",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/w4/lsgx7ykn35x5549kp8vwtzcr0000gn/T/ipykernel_97877/1396537375.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdf\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d17df82-a718-49a7-baa9-a5d0d0b9e676",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
