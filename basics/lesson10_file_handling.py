# ==========================================
# Lesson 10 - File Handling
# ==========================================

# Create and write to a file
with open("aircraft.txt", "w") as file:
    file.write("Aircraft: Airbus A350\n")
    file.write("Engine: Rolls-Royce Trent XWB\n")
    file.write("Cruise Speed: 905 km/h\n")

print("Data written to aircraft.txt")

print("\n--------------------------")

# Read the file
with open("aircraft.txt", "r") as file:
    content = file.read()

print("File Contents:")
print(content)

print("\n--------------------------")

# Add more information to the file
with open("aircraft.txt", "a") as file:
    file.write("Range: 15000 km\n")

print("New information added.")
