def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9.0 / 5.0) + 32.0

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32.0) * 5.0 / 9.0

def main():
    print("====================================")
    print("      Temperature Converter")
    print("====================================")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("====================================")
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        temperature = float(input("\nEnter temperature in Celsius: "))
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"\n{temperature:.2f} Celsius is equal to {converted_temperature:.2f} Fahrenheit")
    elif choice == 2:
        temperature = float(input("\nEnter temperature in Fahrenheit: "))
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"\n{temperature:.2f} Fahrenheit is equal to {converted_temperature:.2f} Celsius")
    else:
        print("\nInvalid choice. Please enter 1 or 2.")
    
    print("\n====================================")

if __name__ == "__main__":
    main()
