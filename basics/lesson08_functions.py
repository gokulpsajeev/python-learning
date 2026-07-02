# Lesson 8 - Functions

# Function to display aircraft information
def aircraft_info():
    print("Aircraft: Airbus A350")
    print("Engine: Rolls-Royce Trent XWB")
    print("Cruise Speed: 905 km/h")

# Call the function
aircraft_info()

print("\n----------------------")

# Function with parameters
def calculate_speed(distance, time):
    speed = distance / time
    print("Average Speed:", speed, "km/h")

calculate_speed(1800, 2)

print("\n----------------------")

# Function that returns a value
def add_thrust(engine1, engine2):
    return engine1 + engine2

total_thrust = add_thrust(350, 360)

print("Total Thrust:", total_thrust, "kN")
