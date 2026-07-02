# ==========================================
# Lesson 9 - Classes
# ==========================================

# Create a class
class Aircraft:

    # Constructor
    def __init__(self, model, engine, speed):
        self.model = model
        self.engine = engine
        self.speed = speed

    # Method
    def display_info(self):
        print("Aircraft Model:", self.model)
        print("Engine:", self.engine)
        print("Cruise Speed:", self.speed, "km/h")


# Create objects
aircraft1 = Aircraft("Airbus A350", "Rolls-Royce Trent XWB", 905)
aircraft2 = Aircraft("Boeing 787", "GEnx", 903)

# Display information
aircraft1.display_info()

print("\n-------------------------\n")

aircraft2.display_info()
