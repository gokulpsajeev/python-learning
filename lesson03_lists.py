# Lesson 3 - Lists

# Create a list of aircraft
aircraft = ["A320", "A330", "A350", "A380", "A220"]

# Print the entire list
print("Aircraft List:", aircraft)

# Print the first aircraft
print("First Aircraft:", aircraft[0])

# Print the last aircraft
print("Last Aircraft:", aircraft[-1])

# Add a new aircraft
aircraft.append("A321")

print("After Adding:", aircraft)

# Remove an aircraft
aircraft.remove("A330")

print("After Removing:", aircraft)

# Print the total number of aircraft
print("Total Aircraft:", len(aircraft))
