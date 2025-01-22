def length_converter():
    print("\nLength Converter")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Miles to Kilometers")
    print("4. Kilometers to Miles")
    print("5. Inches to Centimeters")
    print("6. Centimeters to Inches")
    print("7. Feet to Meters")
    print("8. Meters to Feet")
    choice = int(input("Choose an option: "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        print(f"{value} meters = {value / 1000} kilometers")
    elif choice == 2:
        print(f"{value} kilometers = {value * 1000} meters")
    elif choice == 3:
        print(f"{value} miles = {value * 1.60934} kilometers")
    elif choice == 4:
        print(f"{value} kilometers = {value / 1.60934} miles")
    elif choice == 5:
        print(f"{value} inches = {value * 2.54} centimeters")
    elif choice == 6:
        print(f"{value} centimeters = {value / 2.54} inches")
    elif choice == 7:
        print(f"{value} feet = {value * 0.3048} meters")
    elif choice == 8:
        print(f"{value} meters = {value / 0.3048} feet")
    else:
        print("Invalid choice.")

def weight_converter():
    print("\nWeight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Grams to Kilograms")
    print("4. Kilograms to Grams")
    print("5. Ounces to Grams")
    print("6. Grams to Ounces")
    choice = int(input("Choose an option: "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        print(f"{value} kilograms = {value * 2.20462} pounds")
    elif choice == 2:
        print(f"{value} pounds = {value / 2.20462} kilograms")
    elif choice == 3:
        print(f"{value} grams = {value / 1000} kilograms")
    elif choice == 4:
        print(f"{value} kilograms = {value * 1000} grams")
    elif choice == 5:
        print(f"{value} ounces = {value * 28.3495} grams")
    elif choice == 6:
        print(f"{value} grams = {value / 28.3495} ounces")
    else:
        print("Invalid choice.")

def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice = int(input("Choose an option: "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        print(f"{value}°C = {(value * 9/5) + 32}°F")
    elif choice == 2:
        print(f"{value}°F = {(value - 32) * 5/9}°C")
    elif choice == 3:
        print(f"{value}°C = {value + 273.15} K")
    elif choice == 4:
        print(f"{value} K = {value - 273.15}°C")
    elif choice == 5:
        print(f"{value}°F = {((value - 32) * 5/9) + 273.15} K")
    elif choice == 6:
        print(f"{value} K = {((value - 273.15) * 9/5) + 32}°F")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\nUnit Converter")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        choice = int(input("Choose a conversion type: "))

        if choice == 1:
            length_converter()
        elif choice == 2:
            weight_converter()
        elif choice == 3:
            temperature_converter()
        elif choice == 4:
            print("Exiting the converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
