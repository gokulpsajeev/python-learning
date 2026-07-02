# ==========================================
# Lesson 11 - Exception Handling
# ==========================================

print("Python Exception Handling")

print("\n--------------------------")

# Example 1: Handling division by zero
try:
    number = 100
    divisor = 0
    result = number / divisor
    print(result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

print("\n--------------------------")

# Example 2: Handling invalid list index
aircraft = ["A320", "A350", "A380"]

try:
    print(aircraft[5])

except IndexError:
    print("Error: Aircraft does not exist in the list.")

print("\n--------------------------")

# Example 3: Using finally
try:
    print("Opening file...")

except:
    print("Something went wrong.")

finally:
    print("Program Finished.")
