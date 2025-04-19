# This program performs simple unit conversions for distance, temperature, and weight

def km_to_miles(km):
    return km * 0.621371  # 1 km = 0.621371 miles

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Formula for temperature conversion

def kg_to_pounds(kg):
    return kg * 2.20462  # 1 kg = 2.20462 pounds

def main():
    print("Simple Unit Converter")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    
    choice = input("Enter conversion type (1/2/3): ")
    
    try:
        if choice == '1':
            km = float(input("Enter distance in kilometers: "))
            print(f"{km} km is equal to {km_to_miles(km):.1f} miles")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.1f}°F")
        elif choice == '3':
            kg = float(input("Enter weight in kilograms: "))
            print(f"{kg} kg is equal to {kg_to_pounds(kg):.1f} pounds")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
