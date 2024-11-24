# Author: Nathan Asif | 2024F-BSE-278
# Operations Menu
while True:
    # Menu
    print("\n----- Operations Menu -----:")
    print("1. Calculator")
    print("2. Area of Circle")
    print("3. Temperature Conversion")
    print("4. Even or Odd Checker")
    print("5. Factorial")
    print("6. Exit")

    choice = input("Please select an option (1-6): ")

    if choice == '1':
        # Calculator
        while True:
            print("\n----- Calculator -----")
            num1 = eval(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = eval(input("Enter second number: "))
            
            if operator == '+':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif operator == '-':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif operator == '*':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif operator == '/':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error! Division by zero.")
            else:
                print("Invalid operator!")
            
            # Rerun the program or go back to menu
            cont_calc = input("Do you want to perform another calculation? (yes to continue, any other key to go back to menu): ").lower()
            if cont_calc != 'yes':
                break

    elif choice == '2':
        # Area of Circle
        while True:
            print("\n----- Area of Circle -----")
            radius = float(input("Enter the radius of the circle: "))
            PI = 3.14159
            area = PI * (radius ** 2)
            print(f"Area of the circle with radius {radius} is {round(area, 2)}")
            
            # Rerun the program or go back to menu
            cont_area = input("Do you want to calculate another area? (yes to continue, any other key to go back to menu): ").lower()
            if cont_area != 'yes':
                break

    elif choice == '3':
        # Temperature Conversion

        # Constants for conversion
        CELSIUS_TO_KELVIN = 273.15
        FAHRENHEIT_TO_CELSIUS_SCALE = 5 / 9
        CELSIUS_TO_FAHRENHEIT_SCALE = 9 / 5
        FAHRENHEIT_OFFSET = 32

        while True:
            print("\n----- Temperature Conversion -----")
            temp = float(input("Enter the temperature value: "))
            from_unit = input("Enter the current unit of temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
            to_unit = input("Enter the unit to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

            if from_unit == 'C':
                if to_unit == 'F':
                    # Celsius to Fahrenheit
                    converted = (temp * CELSIUS_TO_FAHRENHEIT_SCALE) + FAHRENHEIT_OFFSET
                    print(f"{temp} Celsius is {round(converted, 2)} Fahrenheit.")
                elif to_unit == 'K':
                    # Celsius to Kelvin
                    converted = temp + CELSIUS_TO_KELVIN
                    print(f"{temp} Celsius is {round(converted, 2)} Kelvin.")
                elif to_unit == 'C':
                    print(f"{temp} Celsius is already in Celsius.")
                else:
                    print("Invalid target unit! Please enter C, F, or K.")
            
            elif from_unit == 'F':
                if to_unit == 'C':
                    # Fahrenheit to Celsius
                    converted = (temp - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_SCALE
                    print(f"{temp} Fahrenheit is {round(converted, 2)} Celsius.")
                elif to_unit == 'K':
                    # Fahrenheit to Kelvin
                    converted = ((temp - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_SCALE) + CELSIUS_TO_KELVIN
                    print(f"{temp} Fahrenheit is {round(converted, 2)} Kelvin.")
                elif to_unit == 'F':
                    print(f"{temp} Fahrenheit is already in Fahrenheit.")
                else:
                    print("Invalid target unit! Please enter C, F, or K.")
            
            elif from_unit == 'K':
                if to_unit == 'C':
                    # Kelvin to Celsius
                    converted = temp - CELSIUS_TO_KELVIN
                    print(f"{temp} Kelvin is {round(converted, 2)} Celsius.")
                elif to_unit == 'F':
                    # Kelvin to Fahrenheit
                    converted = ((temp - CELSIUS_TO_KELVIN) * CELSIUS_TO_FAHRENHEIT_SCALE) + FAHRENHEIT_OFFSET
                    print(f"{temp} Kelvin is {round(converted, 2)} Fahrenheit.")
                elif to_unit == 'K':
                    print(f"{temp} Kelvin is already in Kelvin.")
                else:
                    print("Invalid target unit! Please enter C, F, or K.")
            
            else:
                print("Invalid source unit! Please enter C, F, or K.")

            # Option to repeat or exit
            cont_temp = input("Do you want to convert another temperature? (yes to continue, any other key to go back to menu): ").lower()
            if cont_temp != 'yes':
                break

    elif choice == '4':
        # Even or Odd Checker
        while True:
            print("\n----- Even or Odd Checker -----")
            number = int(input("Enter a number: "))
            
            if number % 2 == 0:
                print(f"{number} is an Even number.")
            else:
                print(f"{number} is an Odd number.")
                
            # Rerun the program or go back to menu
            cont_even_odd = input("Do you want to check another number? (yes to continue, any other key to go back to menu): ").lower()
            if cont_even_odd != 'yes':
                break

    elif choice == '5':
        # Factorial Calculation
        while True:
            print("\n----- Factorial Calculator -----")
            num = eval(input("Enter a number to find its factorial: "))

            if num < 0:
                print("Factorial does not exist for negative numbers.")
            else:
                # Factorial using for loop
                factorial_for = 1
                for i in range(1, num + 1):
                    factorial_for *= i
                print(f"Factorial of {num} using for loop is {factorial_for}")
                
                # Factorial using while loop
                factorial_while = 1
                i = 1
                while i <= num:
                    factorial_while *= i
                    i += 1
                print(f"Factorial of {num} using while loop is {factorial_while}")

            # Rerun the program or go back to menu
            cont_factorial = input("Do you want to calculate another factorial? (yes to continue, any other key to go back to menu): ").lower()
            if cont_factorial != 'yes':
                break

    elif choice == '6':
        # Exit the program
        print("Exiting the program.....")
        break

    else:
        print("Invalid choice! Please select a number between 1 and 6.")