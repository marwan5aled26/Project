# Program Name: Numbering System Convertor
# Program Description: The code converts numbers between decimal, binary, octal, and hexadecimal.
# It has functions for each conversion and uses menus to guide the user through the process of entering a number,
# selecting the base for conversion, and displaying the result.
# Author: Marwan Khaled Sayed Boraey
# Date: 8/3/2024
# Version: 1.0

# Function to convert decimal to binary
def decimal_to_binary(decimal_number):
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number //= 2
    return binary_number if binary_number else "0"


# Function to convert decimal to octal
def decimal_to_octal(decimal_number):
    octal_number = ""
    while decimal_number > 0:
        octal_number = str(decimal_number % 8) + octal_number
        decimal_number //= 8
    return octal_number if octal_number else "0"


# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(decimal_number):
    hexadecimal_number = ""
    hex_chars = "0123456789ABCDEF"
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_number = hex_chars[remainder] + hexadecimal_number
        decimal_number //= 16
    return hexadecimal_number if hexadecimal_number else "0"


# Function to convert binary to decimal
def binary_to_decimal(binary_number):
    decimal_number = 0
    power = 0
    while binary_number:
        decimal_number += (binary_number % 10) * (2 ** power)
        binary_number //= 10
        power += 1
    return decimal_number


# Function to convert binary to octal
def binary_to_octal(binary_number):
    decimal_number = binary_to_decimal(binary_number)
    octal_number = ""
    while decimal_number > 0:
        octal_number = str(decimal_number % 8) + octal_number
        decimal_number //= 8
    return octal_number if octal_number else "0"


# Function to convert binary to hexadecimal
def binary_to_hexadecimal(binary_number):
    decimal_number = binary_to_decimal(binary_number)
    hexadecimal_number = ""
    hex_chars = "0123456789ABCDEF"
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_number = hex_chars[remainder] + hexadecimal_number
        decimal_number //= 16
    return hexadecimal_number if hexadecimal_number else "0"


# Function to convert octal to decimal
def octal_to_decimal(octal_number):
    decimal_number = 0
    power = 0
    while octal_number:
        decimal_number += (octal_number % 10) * (8 ** power)
        octal_number //= 10
        power += 1
    return decimal_number


# Function to convert octal to binary
def octal_to_binary(octal_number):
    decimal_number = octal_to_decimal(octal_number)
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number //= 2
    return binary_number if binary_number else "0"


# Function to convert octal to hexadecimal
def octal_to_hexadecimal(octal_number):
    decimal_number = octal_to_decimal(octal_number)
    hexadecimal_number = ""
    hex_chars = "0123456789ABCDEF"
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_number = hex_chars[remainder] + hexadecimal_number
        decimal_number //= 16
    return hexadecimal_number if hexadecimal_number else "0"


# Function to convert hexadecimal to decimal
def hexadecimal_to_decimal(hexadecimal_number):
    decimal_number = 0
    hex_chars = "0123456789ABCDEF"
    for char in hexadecimal_number:
        decimal_number = decimal_number * 16 + hex_chars.index(char)
    return decimal_number


# Function to convert hexadecimal to binary
def hexadecimal_to_binary(hexadecimal_number):
    decimal_number = hexadecimal_to_decimal(hexadecimal_number)
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number //= 2
    return binary_number if binary_number else "0"


# Function to convert hexadecimal to octal
def hexadecimal_to_octal(hexadecimal_number):
    decimal_number = hexadecimal_to_decimal(hexadecimal_number)
    octal_number = ""
    while decimal_number > 0:
        octal_number = str(decimal_number % 8) + octal_number
        decimal_number //= 8
    return octal_number if octal_number else "0"


while True:  # Menu 1
    print("** Numbering System Converter **")
    print("A) Insert a new number")
    print("B) Exit program")

    choice_menu1 = input("Please select a choice (A/B): ").upper()  # Select a choice

    if choice_menu1 == 'A':
        number = input("Please insert a number: ")

        # Menu 2
        print("** Please select the base you want to convert a number from: **")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")

        choice_menu2 = input("Please select a choice (A/B/C/D): ").upper()  # Select a choice

        if choice_menu2 in ['A', 'B', 'C', 'D']:
            # Menu 3
            print("** Please select the base you want to convert a number to: **")
            print("A) Decimal")
            print("B) Binary")
            print("C) Octal")
            print("D) Hexadecimal")

            choice_menu3 = input("Please select a choice (A/B/C/D): ").upper()# Select a choice

            if choice_menu3 in ['A', 'B', 'C', 'D']:
                result = None  # Initialize result

                # Perform the conversion based on user choices
                if choice_menu2 == 'A':
                    # Convert from Decimal to other bases
                    if choice_menu3 == 'A':
                        result = str(number)
                    elif choice_menu3 == 'B':
                        result = decimal_to_binary(number)
                    elif choice_menu3 == 'C':
                        result = decimal_to_octal(number)
                    elif choice_menu3 == 'D':
                        result = decimal_to_hexadecimal(number)

                elif choice_menu2 == 'B':
                    # Convert from Binary to other bases
                    if choice_menu3 == 'A':
                        result = binary_to_decimal(number)
                    elif choice_menu3 == 'B':
                        result = str(number)
                    elif choice_menu3 == 'C':
                        result = binary_to_octal(number)
                    elif choice_menu3 == 'D':
                        result = binary_to_hexadecimal(number)

                elif choice_menu2 == 'C':
                    # Convert from Octal to other bases
                    if choice_menu3 == 'A':
                        result = octal_to_decimal(number)
                    elif choice_menu3 == 'B':
                        result = octal_to_binary(number)
                    elif choice_menu3 == 'C':
                        result = str(number)
                    elif choice_menu3 == 'D':
                        result = octal_to_hexadecimal(number)

                elif choice_menu2 == 'D':
                    # Convert from Hexadecimal to other bases
                    if choice_menu3 == 'A':
                        result = hexadecimal_to_decimal(number)
                    elif choice_menu3 == 'B':
                        result = hexadecimal_to_binary(number)
                    elif choice_menu3 == 'C':
                        result = hexadecimal_to_octal(number)
                    elif choice_menu3 == 'D':
                        result = str(number)

                print("The result:", result)  # Display the result

            else:
                print("Error: Please select a valid choice.")  # Invalid choice in Menu 3

        else:
            print("Error: Please select a valid choice.")  # Invalid choice in Menu 2

    elif choice_menu1 == 'B':
        break  # Exit the program

    else:  # Invalid choice in Menu 1
        print("Error: Please select a valid choice.")
