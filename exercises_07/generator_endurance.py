def calculate_endurance(fuel, fuel_consumption):
    """
    Calculate the remaining endurance in minutes.

    Parameters:
    - fuel: Fuel in litres
    - fuel_consumption: Fuel consumption in litres per minute

    Returns:
    - Remaining endurance in minutes
    - None if there is a division by zero error or if the input values are not valid
    """
    try:
        # Check if fuel_consumption is not zero (avoid division by zero)
        if fuel_consumption != 0:
            endurance = fuel / fuel_consumption
            return endurance
        else:
            # Handle division by zero error
            raise ValueError("Fuel consumption cannot be zero.")
    except ValueError as e:
        # Handle any other value errors
        print(f"Error: {e}")
        return None

# Calculate fuel consumption
fuel_litres = 3080
fuel_consumption_per_minute = 2

remaining_endurance = calculate_endurance(fuel_litres, fuel_consumption_per_minute)
remaining_endurance_hours = remaining_endurance/60
remaining_endurance_days = remaining_endurance_hours/24

if remaining_endurance is not None:
    print(f"Remaining Endurance: {remaining_endurance} minutes")
    print(f"Remaining Endurance: {remaining_endurance_hours} hours")
    print(f"Remaining Endurance: {remaining_endurance_days} days")
else:
    print("Error calculating endurance.")
