# Lesson 7 - Loops

# List of aircraft
aircraft = ["A320", "A330", "A350", "A380", "A220"]

# Print each aircraft using a for loop
print("Aircraft List:")

for plane in aircraft:
    print(plane)

print("\n----------------------")

# Print engine test numbers
print("Engine Test Numbers:")

for test in range(1, 6):
    print("Test", test)

print("\n----------------------")

# Countdown using a while loop
count = 5

print("Countdown:")

while count > 0:
    print(count)
    count -= 1

print("Takeoff!")
