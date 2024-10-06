# Dictionaries for significant digits, multipliers, tolerance, and temperature coefficient
color_digit = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
}
color_multiplier = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
    "green": 100000, "blue": 1000000, "violet": 10000000,
    "gray": 100000000, "white": 1000000000, "gold": 0.1, "silver": 0.01
}

color_tolerance = {
    "brown": 1, "red": 2, "green": 0.5,"orange":3, "blue": 0.25, "violet": 0.1,
    "gray": 0.05, "gold": 5, "silver": 10,"yellow":4, "none": 20
}

color_temp_coeff = {
    "brown": 100, "red": 50, "orange": 15, "yellow": 25, "blue": 10, "violet": 5
}

# Function to get the resistor colors from the user
def get_resistor_value():
    # Ask the user how many bands the resistor has
    num_bands = int(input("How many color bands does the resistor have? (3, 4, 5, or 6): "))
    
    # Create a list to store the color bands
    bands = []
    
    # Get the color inputs for the respective bands
    for i in range(num_bands):
        color = input(f"Enter color for band {i+1}: ").lower()
        bands.append(color)
    
    return bands, num_bands

# Function to calculate and display the resistance value
def calculate_resistor_value():
    # Retrieve the resistor bands and number of bands
    bands, num_bands = get_resistor_value()

    try:
        # Handling for 3-band, 4-band, 5-band, and 6-band resistors
        if num_bands == 3:
            # 3 bands: 1 significant digit + multiplier + tolerance
            significant_digits = color_digit[bands[0]]
            multiplier_band = bands[1]
            tolerance_band = bands[2]
            
        elif num_bands == 4:
            # 4 bands: 2 significant digits + multiplier + tolerance
            significant_digits = color_digit[bands[0]] * 10 + color_digit[bands[1]]
            multiplier_band = bands[2]
            tolerance_band = bands[3]
        
        elif num_bands == 5:
            # 5 bands: 3 significant digits + multiplier + tolerance
            significant_digits = color_digit[bands[0]] * 100 + color_digit[bands[1]] * 10 + color_digit[bands[2]]
            multiplier_band = bands[3]
            tolerance_band = bands[4]
        
        elif num_bands == 6:
            # 6 bands: 3 significant digits + multiplier + tolerance + temperature coefficient
            significant_digits = color_digit[bands[0]] * 100 + color_digit[bands[1]] * 10 + color_digit[bands[2]]
            multiplier_band = bands[3]
            tolerance_band = bands[4]
            temperature_coeff_band = bands[5]
            temperature_coeff = color_temp_coeff.get(temperature_coeff_band, "Invalid")
        
        # Get multiplier and tolerance values
        multiplier = color_multiplier[multiplier_band]
        tolerance = color_tolerance.get(tolerance_band, "Invalid")
        
        # Calculate resistance value
        resistance_value = significant_digits * multiplier
        
        # Display the calculated resistance for different cases
        if num_bands == 6:
            if temperature_coeff != "Invalid":
                print(f"The resistance value is: {resistance_value} ohms with ±{tolerance}% tolerance and {temperature_coeff} ppm/°C temperature coefficient.")
            else:
                print(f"The resistance value is: {resistance_value} ohms with ±{tolerance}% tolerance.")
        else:
            print(f"The resistance value is: {resistance_value} ohms with ±{tolerance}% tolerance.")
    
    except KeyError:
        print("One or more invalid color names. Please check the colors and try again.")

# Run the program
calculate_resistor_value()

