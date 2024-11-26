import random
import math

def calculate_random_circle_area():
    
    radius = random.uniform(1, 100)
    
    area = math.pi * radius**2
    
    return radius, area

# Example usage
radius, area = calculate_random_circle_area()
print(f"Radius: {radius:.2f}")
print(f"Area: {area:.2f}")
