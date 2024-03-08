# Program Name: Binary System Calculator
# Program Description: The code displays and compute addition and subtraction for two binary numbers,
# and also display and compute one's complement and two's complement for any binary number.
# Author: Marwan Khaled Sayed Boraey
# Date: 8/3/2024
# Version: 1.0

def valid_binary(number):  # Check if the given string is a valid binary number
    return all(bit == '0' or bit == '1' for bit in number)


def ones_complement(binary_number):  # Compute the one's complement of a binary number
    return ''.join('1' if bit == '0' else '0' for bit in binary_number)


def twos_complement(binary_number):
    if not all(bit in '01' for bit in binary_number):  # Check if the binary string is valid
        raise ValueError("Invalid binary string")

    n = len(binary_number)  # Find the length of the binary number
    i = n - 1  # Find the rightmost occurrence of '1'
    while i >= 0 and binary_number[i] != '1':
        i -= 1
    if i == -1:   # If no '1' is found, the original number is zero, and its two's complement is itself
        return binary_number
    result = ''  # Flip the bits to the left of the rightmost '1'
    for j in range(i):
        result += '1' if binary_number[j] == '0' else '0'
    result += binary_number[i:]  # Add the rightmost '1' and the remaining bits as they are
    return result


def binary_addition(num1, num2):
    # Determine the maximum length of the binary numbers
    if len(num1) > len(num2):
        maxlen = len(num1)
    elif len(num1) < len(num2):
        maxlen = len(num2)
    else:
        maxlen = len(num1)

    carry = 0  # Initialize the carry to 0
    result = ""  # Initialize the result string
    num1 = num1.zfill(maxlen)  # Pad the binary numbers with leading zeros if necessary
    num2 = num2.zfill(maxlen)

    for i in range(maxlen - 1, -1, -1):  # Iterate through the binary numbers from right to left
        bits_sum = int(num1[i]) + int(num2[i]) + carry  # Sum of bits at the current position
        result = str(bits_sum % 2) + result  # Append the sum modulo 2 to the result
        carry = bits_sum // 2  # Update the carry for the next iteration

    if carry:  # If there's a carry left after the loop, add it to the front of the result
        result = "1" + result
    return result


def binary_subtraction(num1, num2):
    # Determine the maximum length of the binary numbers
    if len(num1) > len(num2):
        maxlen = len(num1)
    elif len(num1) < len(num2):
        maxlen = len(num2)
    else:
        maxlen = len(num1)

    num1 = num1.zfill(maxlen)  # Pad the binary numbers with leading zeros if necessary
    num2 = num2.zfill(maxlen)
    borrow = 0  # Initialize the borrow to 0
    result = ""  # Initialize the result string

    for i in range(maxlen - 1, -1, -1):  # Iterate through the binary numbers from right to left
        bits = int(num1[i]) - int(num2[i]) - borrow  # Difference of bits at the current position
        if bits < 0:
            bits += 2  # If the result is negative, add 2 to adjust
            borrow = 1  # Set borrow for the next iteration
        else:
            borrow = 0  # Reset borrow if no adjustment is needed
        result = str(bits) + result  # Append the result to the front

    if borrow:  # If there's a borrow left after the loop, add it to the front of the result
        result = "1" + result
    return result


while True:  # Start the main program loop
    # Menu 1:
    print("** Binary Calculator **")
    print("A) Insert new numbers")
    print("B) Exit")

    choice_menu1 = input("Please select a choice (A/B): ").upper()  # Insert a choice from Menu 1

    if choice_menu1 == 'A':  # Input for the first binary number
        binary_number1 = input("Please insert the first binary number: ").upper()

        if valid_binary(binary_number1):  # Validate the first binary number
            # Menu 2:
            print("** Please select the operation **")
            print("A) Compute one's complement")
            print("B) Compute two's complement")
            print("C) Addition")
            print("D) Subtraction")

            choice_menu2 = input("Please select a choice (A/B/C/D): ").upper()  # Insert a choice from Menu 2

            if choice_menu2 == 'A':  # Compute and display one's complement
                result = ones_complement(binary_number1).upper()
                print("The one's complement is:", result)

            elif choice_menu2 == 'B':   # Compute and display two's complement
                result = twos_complement(binary_number1).upper()
                print("The two's complement is:", result)

            elif choice_menu2 in ['C', 'D']:  # Input for the second binary number
                binary_number2 = input("Please insert the second binary number: ").upper()

                if valid_binary(binary_number2):  # Validate the second binary number
                    if choice_menu2 == 'C':  # Compute and display binary addition
                        result = binary_addition(binary_number1, binary_number2)
                        print("The sum is:", result)

                    elif choice_menu2 == 'D':  # Compute and display binary subtraction
                        result = binary_subtraction(binary_number1, binary_number2)
                        print("The difference is:", result)

                else:  # Invalid second binary number
                    print("Error: Please insert a valid binary number for the second input.")

            else:  # Invalid choice in Menu 2
                print("Error: Please select a valid choice.")

        else:  # Invalid first binary number
            print("Error: Please insert a valid binary number for the first input.")

    elif choice_menu1 == 'B':  # Exit the program
        break

    else:  # Invalid choice in Menu 1
        print("Error: Please select a valid choice.")
        