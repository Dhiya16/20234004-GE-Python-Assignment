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

def validate_name(name):
    try:

        if any(char.isdigit() for char in name):
            raise ValueError("Name should not contain digits.")


        if not name.isalpha():
            raise ValueError("Name should only contain alphabetic characters.")


        print(f"Entered name: {name}")

    except ValueError as e:
        print(f"Error: {e}")

user_name = input("Enter your name: ")
validate_name(user_name)
