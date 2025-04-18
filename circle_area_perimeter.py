"""
This program calculates the area and perimeter (circumference) of a circle.
The user provides the radius, and the program returns both results.
"""

import math  # Import the math module for the constant pi

def calculate_circle(radius):
    area = math.pi * radius ** 2  # Formula for area
    perimeter = 2 * math.pi * radius  # Formula for circumference
    return area, perimeter

if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))  # Ask user for the radius
        if radius < 0:
            print("Radius can't be negative. Please enter a positive value.")
        else:
            area, perimeter = calculate_circle(radius)
            print(f"Area of the circle: {area:.1f}")
            print(f"Circumference of the circle: {perimeter:.1f}")
    except ValueError:
        print("Invalid input. Please enter a number.")
