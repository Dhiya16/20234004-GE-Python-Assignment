#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     11-12-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def analyze_character(char):
    if char.isalpha():
        if char.isupper():
            print(f"The character '{char}' is an uppercase letter.")
        else:
            print(f"The character '{char}' is a lowercase letter.")
    elif char.isdigit():
        number_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        digit_name = number_names[int(char)]
        print(f"The character '{char}' is a numeric digit, and its name is {digit_name}.")
    else:
        print(f"The character '{char}' is a special character.")


user_input = input("Enter a character: ")

analyze_character(user_input)