# Define conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometer_to_miles(kilometeres):
    return kilometeres * 0.62137

def miles_to_kilometers(miles):
    return miles / 0.62137

# function to handle user input and perform unit conversions
def unit_convertor():
    print("Welcome to the Unit Convertor!")
    print("Please select the conversion type:")
    print("1. Temperature (Celsius to Fahrenheit)")
    print("2. Temperature (Fahrenheit to Celsius)")
    print("3. Distance (Kilometers to Miles)")
    print("4. Distance (Miles to Kilometers)")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    elif choice == "3":
        kilometers = float(input("Enter distance in Kilometers: "))
        miles = kilometer_to_miles(kilometers)
        print(f"{kilometers} km is equal to {miles:.2f} miles")
    elif choice == "4":
        miles = float(input("Enter distance in Miles: "))
        kilometers = miles_to_kilometers(miles)
        print(f"{miles:.2f} miles is equal to {kilometers:.2f} km")
    else:
        print("Invalid choice. Please try again.")
        
unit_convertor()