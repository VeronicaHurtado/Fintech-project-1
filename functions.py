from data_collection import get_distance, get_car_emissions_rate


# Calculate the cost of the trip based on distance, fuel_type and cost_per_litre
# distance: a float indicating the distance in kilometres for the given trip
# fuel_type: a string indicating the type of fuel used (either "petrol" or "diesel")
# cost_per_litre: a float indicating the cost of fuel per litre (in dollars)
def calculate_fuel_cost(distance, fuel_type, cost_per_litre):
    # @ToDo: Replace with kilometres per litre based on Car Make and Model from get_fuel_consumption
    # @ToDo: Consider average speed
    if fuel_type == "petrol":
        # Assume fuel consumption is 12.5 kilometres per litre
        kml = 12.5
    elif fuel_type == "diesel":
        # Assume fuel consumption is 15.5 kilometres per litre
        kml = 15.5
    else:
        # Raise an error for unsupported fuel types
        raise ValueError(f"Unsupported fuel type: {fuel_type}")

    print(f'Distance: {distance} km. Fuel consumption: {kml} kml')

    # Calculate the number of litres consumed
    litres_consumed = distance / kml
    # Calculate the cost of the fuel consumed
    fuel_cost = litres_consumed * cost_per_litre
    return fuel_cost


# Calculate the fuel cost between two locations based on fuel type
# start_location: a string indicating the address for the starting point (e.g. "1 Collins Street, Melbourne, VIC")
# end_location: a string indicating the address for the ending point (e.g., "1 Elizabeth Street, Melbourne, VIC")
# fuel_type: a string indicating the type of fuel used (either "petrol" or "diesel")
def calculate_trip_fuel_cost(fuel_type, distance):
    # @ToDo: Get fuel cost per litre from the APIs
    cost_per_litre = 2.50  # Assume this price for now
    # Calculate total fuel cost for this distance
    cost = calculate_fuel_cost(distance=distance, fuel_type=fuel_type, cost_per_litre=cost_per_litre)
    return cost


# Calculate the emissions saved by not using a car
def calculate_emissions_saved(distance, car_make, car_model):
    car_emissions_rate = get_car_emissions_rate()
    emissions_saved = distance * car_emissions_rate
    return emissions_saved


