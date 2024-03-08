Numbering System Convertor
START
FUNCTION decimal_to_binary(decimal_number):
IF NOT (decimal_number is an integer and decimal_number >= 0):
RAISE ValueError("Invalid decimal number input. Must be a non-negative integer")
IF decimal_number == 0:
RETURN "0"
SET binary_number TO ""
WHILE decimal_number > 0:
SET binary_number TO STR(decimal_number % 2) + binary_number
SET decimal_number TO decimal_number //2
RETURN binary_number
FUNCTION decimal_to_octal(decimal_number):
IF NOT (decimal_number is an integer and decimal_number >= 0):
RAISE ValueError("Invalid decimal number input. Must be a non-negative integer")
IF decimal_number == 0:
RETURN "0"
SET octal_digits TO []
WHILE decimal_number > 0:
SET remainder TO decimal_number % 8
octal_digits.append(STR(remainder))
SET decimal_number TO decimal_number 8
octal_digits.reverse()
SET octal_representation TO "".join(octal_digits)
RETURN octal_representation
FUNCTION decimal_to_hexadecimal(decimal_number):
IF NOT (decimal_number is an integer and decimal_number >= 0):
RAISE ValueError("Invalid decimal number input. Must be a non-negative integer")
IF decimal_number == 0:
RETURN "0"
SET hexadecimal TO ""
WHILE decimal_number > 0:
SET remainder TO decimal_number % 16
SET hexadecimal TO hexa_digits[remainder] + hexadecimal
SET decimal_number TO decimal_number //16
RETURN hexadecimal
FUNCTION binary_to_octal(binary_number):
IF NOT ALL(bit in '01' for bit in binary_number):
RAISE ValueError("Invalid binary number")
WHILE LEN(binary_number) % 3 != 0:
SET binary_number TO '0' + binary_number
SET octal_digits TO []
FOR i IN RANGE(0, len(binary_number), 3):
SET three_bits TO list(binary_number[i:i+3])
three_bits.reverse()
SET decimal_value TO 0
FOR index, element in enumerate(three_bits):
SET decimal_value TO decimal_value + int(element) * (2**index)
octal_digits.append(str(decimal_value))
SET octal_representation TO "".join(octal_digits)
RETURN octal_representation
FUNCTION binary_to_decimal(binary_number):
IF NOT ALL(bit in '01' for bit in binary_number):
RAISE ValueError("Invalid binary number")
SET array TO list(binary_number)
array.reverse()
SET decimal TO 0
FOR power, digit in enumerate(array):
SET decimal TO decimal + int(digit) * 2**power
RETURN decimal
FUNCTION binary_to_hexadecimal(binary_number):
IF NOT ALL(bit in '01' for bit in binary_number):
RAISE ValueError("Invalid binary number")
SET decimal_number TO binary_to_decimal(binary_number)
SET hexadecimal TO decimal_to_hexadecimal(decimal_number)
RETURN hexadecimal
FUNCTION hexadecimal_to_octal(hexadecimal_number):
SET decimal_number TO hexadecimal_to_decimal(hexadecimal_number)
SET octal_number TO decimal_to_octal(decimal_number)
RETURN octal_number
FUNCTION hexadecimal_to_decimal(hexadecimal_number):
IF NOT ALL(char.isdigit() or char.upper() in 'ABCDEF' for char in hexadecimal_number):
RAISE ValueError("Invalid hexadecimal number")
SET array TO list(str(hexadecimal_number).upper())
array.reverse()
SET decimal TO 0
FOR i in RANGE(LEN(array)):
SET decimal TO decimal + hexa_digits.index(array[i]) * (16 ** i)
RETURN decimal
FUNCTION hexadecimal_to_binary(hexadecimal_number):
SET decimal_number TO hexadecimal_to_decimal(hexadecimal_number)
SET binary_number TO decimal_to_binary(decimal_number)
RETURN binary_number
FUNCTION octal_to_decimal(number):
IF NOT ALL(char.isdigit() and int(char) < 8 for char in str(number)):
RAISE ValueError("Invalid octal number")
SET decimal TO 0
SET power TO 0
WHILE int(number) > 0:
SET remainder TO INT(number) % 10
SET decimal TO decimal + remainder * 8 ** power
SET power TO power + 1
SET number TO INT(number) // 10
RETURN decimal
FUNCTION octal_to_hexadecimal(number):
SET number TO octal_to_decimal(number)
SET hexadecimal TO decimal_to_hexadecimal(number)
RETURN hexadecimal
FUNCTION octal_to_binary(octal_number):
SET octal_number TO octal_to_decimal(octal_number)
SET binary_number TO decimal_to_binary(octal_number)
RETURN binary_number
WHILE True:
PRINT("** Numbering System Converter **")
PRINT("A) Insert a new number")
PRINT("B) Exit program")
SET choice_menu1 TO GET("Please select a choice (A/B): ").upper()
IF choice_menu1 == 'A':
SET number TO GET("Please insert a number: ")
PRINT("** Please select the base you want to convert a number from: **")
PRINT("A) Decimal")
PRINT("B) Binary")
PRINT("C) Octal")
PRINT("D) Hexadecimal")
SET choice_menu2 TO GET("Please select a choice (A/B/C/D): ").upper()
IF choice_menu2 in ['A', 'B', 'C', 'D']:
PRINT("** Please select the base you want to convert a number to: **")
PRINT("A) Decimal")
PRINT("B) Binary")
PRINT("C) Octal")
PRINT("D) Hexadecimal")
SET choice_menu3 TO GET("Please select a choice (A/B/C/D): ").upper()
IF choice_menu3 in ['A', 'B', 'C', 'D']:
SET result TO None
IF choice_menu2 == 'A':
IF choice_menu3 == 'A':
SET result TO int(number)
ELSE IF choice_menu3 == 'B':
SET result TO decimal_to_binary(int(number))
ELSE IF choice_menu3 == 'C':
SET result TO decimal_to_octal(int(number))
ELSE IF choice_menu3 == 'D':
SET result TO decimal_to_hexadecimal(int(number))
ELSE IF choice_menu2 == 'B':
IF choice_menu3 == 'A':
SET result TO binary_to_decimal(number)
ELSE IF choice_menu3 == 'B':
SET result TO int(number)
ELSE IF choice_menu3 == 'C':
SET result TO binary_to_octal(number)
ELSE IF choice_menu3 == 'D':
SET result TO binary_to_hexadecimal(number)
ELSE IF choice_menu2 == 'C':
IF choice_menu3 == 'A':
SET result TO octal_to_decimal(number)
ELSE IF choice_menu3 == 'B':
SET result TO octal_to_binary(number)
ELSE IF choice_menu3 == 'D':
SET result TO octal_to_hexadecimal(number)
ELSE IF choice_menu2 == 'D':
IF choice_menu3 == 'A':
SET result TO hexadecimal_to_decimal(number)
ELSE IF choice_menu3 == 'B':
SET result TO hexadecimal_to_binary(number)
ELSE IF choice_menu3 == 'C':
SET result TO hexadecimal_to_octal(number)
ELSE IF choice_menu3 == 'D':
SET result TO number
PRINT("The result:", result)
ELSE:
PRINT("Error: Please select a valid choice.")
ELSE:
PRINT("Error: Please select a valid choice.")
ELSE IF choice_menu1 == 'B':
PRINT("Exiting program.bye.")
BREAK
ELSE:
PRINT("Error: Please select a valid choice.")
Binary System Calculator
START
FUNCTION binary_to_decimal(binary_number):
IF NOT ALL(bit in '01' for bit in binary_number):
RAISE ValueError("Invalid binary number")
SET array TO list(binary_number)
array.reverse()
SET decimal TO 0
FOR power, digit in enumerate(array):
SET decimal TO decimal + int(digit) * 2**power
RETURN decimal
FUNCTION valid_binary(number)
RETURN ALL (bit == '0' OR bit == '1' FOR EACH bit IN number END FOR)
END FUNCTION
FUNCTION ones_complement(binary_number)
RETURN JOIN ('1' IF bit == '0' ELSE '0' FOR EACH bit IN binary_number END FOR)
END FUNCTION
FUNCTION twos_complement(binary_number)
IF NOT ALL (bit IN '01' FOR EACH bit IN binary_number END FOR) THEN
RAISE ValueError ("Invalid binary string")
END IF
SET n TO LENGTH (binary_number)
SET i TO n - 1
WHILE i >= 0 AND binary_number[i]! = '1'
SET i TO i - 1
END WHILE
IF i == -1 THEN
RETURN binary_number
END IF
SET result TO ''
FOR j FROM 0 TO i - 1
SET result TO result + ('1' IF binary_number[j] == '0' ELSE '0')
END FOR
RETURN result + binary_number[i:]
FUNCTION binary_addition(num1, num2)
SET maxlen TO MAX (LENGTH (num1), LENGTH (num2))
SET carry TO 0
SET result TO ""
SET num1 TO ZFILL (num1, maxlen)
SET num2 TO ZFILL (num2, maxlen)
FOR i FROM maxlen - 1 TO 0 STEP -1
SET bits_sum TO INT (num1[i]) + INT (num2[i]) + carry
SET result TO STRING (bits_sum % 2) + result
SET carry TO bits_sum // 2
END FOR
IF carry!= 0
SET result TO "1" + result
END IF
RETURN result
END FUNCTION
FUNCTION binary_subtraction (num1, num2)
SET maxlen TO MAX (LENGTH (num1), LENGTH (num2))
SET num1 TO ZFILL (num1, maxlen)
SET num2 TO ZFILL (num2, maxlen)
IF binary_to_decimal(num1) < binary_to_decimal(num2):
RAISE ValueError("Cannot subtract a larger number from a smaller number")
SET borrow TO 0
SET result TO ""
FOR i FROM maxlen - 1 TO 0 STEP -1
SET bits TO INTEGER (num1[i]) – INTEGER (num2[i]) - BORROW
IF bits < 0
SET bits TO bits + 2
SET borrow TO 1
ELSE
SET borrow TO 0
END IF
SET result TO STRING (bits) + result
END FOR
IF BORROW! = 0
SET result TO "1" + result
END IF
RETURN result
END FUNCTION
WHILE TRUE
PRINT "** Binary Calculator **"
PRINT "A) Insert new numbers"
PRINT "B) Exit"
SET choice_menu1 TO GET ("Please select a choice (A/B): "). UPPER ()
IF choice_menu1 EQUALS 'A' THEN
SET binary_number1 TO GET ("Please insert the first binary number: "). UPPER ()
IF valid_binary(binary_number1) THEN
# Menu 2
PRINT "** Please select the operation **"
PRINT "A) Compute one's complement"
PRINT "B) Compute two's complement"
PRINT "C) Addition"
PRINT "D) Subtraction"
SET choice_menu2 TO GET ("Please select a choice (A/B/C/D): "). UPPER ()
IF choice_menu2 EQUALS 'A' THEN
SET result TO ones_complement(binary_number1)
PRINT "The one's complement is:", result
ELSE IF choice_menu2 EQUALS 'B' THEN
SET result TO twos_complement(binary_number1)
PRINT "The two's complement is:", result
ELSE IF choice_menu2 IN ['C', 'D'] THEN
SET binary_number2 TO GET ("Please insert the second binary number: "). UPPER ()
IF valid_binary(binary_number2) THEN
IF choice_menu2 EQUALS 'C' THEN
SET result TO binary_addition (binary_number1, binary_number2)
PRINT "The sum is:", result
ELSE IF choice_menu2 EQUALS 'D' THEN
SET result TO binary_subtraction (binary_number1, binary_number2)
PRINT "The difference is:", result
END IF
ELSE
PRINT "Error: Please insert a valid binary number for the second input."
END IF
ELSE
PRINT "Error: Please select a valid choice in Menu 2."
END IF
ELSE
PRINT "Error: Please insert a valid binary number for the first input."
END IF
ELSE IF choice_menu1 EQUALS 'B' THEN
BREAK
ELSE
PRINT "Error: Please select a valid choice in Menu 1."
END IF
END WHILE
END
