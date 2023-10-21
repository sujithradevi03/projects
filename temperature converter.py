def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

while True:
    print("Choose an option:")
    print("1. Convert from Celsius")
    print("2. Convert from Fahrenheit")
    print("3. Convert from Kelvin")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit: {:.2f}".format(celsius_to_fahrenheit(celsius)))
        print("Temperature in Kelvin: {:.2f}".format(celsius_to_kelvin(celsius)))
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius: {:.2f}".format(fahrenheit_to_celsius(fahrenheit)))
        print("Temperature in Kelvin: {:.2f}".format(fahrenheit_to_kelvin(fahrenheit)))
    elif choice == '3':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print("Temperature in Celsius: {:.2f}".format(kelvin_to_celsius(kelvin)))
        print("Temperature in Fahrenheit: {:.2f}".format(kelvin_to_fahrenheit(kelvin)))
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4)")
