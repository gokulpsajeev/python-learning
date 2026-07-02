# ==========================================
# Lesson 12 - Modules & Packages
# ==========================================

# Import the built-in math module
import math

print("Square Root of 81:", math.sqrt(81))
print("Value of Pi:", math.pi)

print("\n--------------------------")

# Import specific functions
from math import pow, factorial

print("5 raised to the power of 3:", pow(5, 3))
print("Factorial of 5:", factorial(5))

print("\n--------------------------")

# Import the random module
import random

print("Random Number:", random.randint(1, 100))

print("\n--------------------------")

# Import the datetime module
import datetime

today = datetime.datetime.now()

print("Current Date and Time:")
print(today)
