# Sample list of temperatures in Kelvin
kelvin_temperatures = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390]

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Displaying temperatures in Kelvin, Celsius, and Fahrenheit
for kelvin in kelvin_temperatures:
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Kelvin: {kelvin} K, Celsius: {celsius:.2f} °C, Fahrenheit: {fahrenheit:.2f} °F")
