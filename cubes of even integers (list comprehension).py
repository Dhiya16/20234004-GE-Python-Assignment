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

def cubes_of_even_numbers_list_comprehension(input_list):
    return [element**3 for element in input_list if isinstance(element, int) and element % 2 == 0]

input_list = [4,78,7,89]
result_list_comprehension = cubes_of_even_numbers_list_comprehension(input_list)
print("Result using list comprehension:", result_list_comprehension)