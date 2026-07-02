# Lesson 6 - Sets

# Create a set of aircraft manufacturers
manufacturers = {"Airbus", "Boeing", "Embraer", "Bombardier"}

# Print the set
print("Manufacturers:", manufacturers)

# Add a new manufacturer
manufacturers.add("COMAC")

print("\nAfter Adding COMAC:")
print(manufacturers)

# Remove a manufacturer
manufacturers.remove("Bombardier")

print("\nAfter Removing Bombardier:")
print(manufacturers)

# Check if an item exists
print("\nIs Airbus in the set?")
print("Airbus" in manufacturers)

# Number of items
print("\nTotal Manufacturers:", len(manufacturers))

# Display the data type
print("\nData Type:", type(manufacturers))
