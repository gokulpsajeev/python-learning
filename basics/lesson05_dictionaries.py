# Lesson 5 - Dictionaries

# Create a dictionary containing aircraft information
aircraft = {
    "Model": "Airbus A350",
    "Engine": "Rolls-Royce Trent XWB",
    "Cruise Speed": 905,
    "Range": 15000,
    "Passengers": 350
}

# Print the entire dictionary
print("Aircraft Information:")
print(aircraft)

# Access individual values
print("Model:", aircraft["Model"])
print("Engine:", aircraft["Engine"])
print("Cruise Speed:", aircraft["Cruise Speed"], "km/h")

# Add a new key-value pair
aircraft["Manufacturer"] = "Airbus"

print("\nAfter Adding Manufacturer:")
print(aircraft)

# Update an existing value
aircraft["Passengers"] = 325

print("\nAfter Updating Passengers:")
print(aircraft)

# Print all keys
print("\nKeys:")
print(aircraft.keys())

# Print all values
print("\nValues:")
print(aircraft.values())
