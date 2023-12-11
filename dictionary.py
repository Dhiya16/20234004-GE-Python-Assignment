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

def generate_cubes_dictionary():
    cubes_dict = {key: key**3 for key in range(1, 6)}
    print("Generated Dictionary:")
    print(cubes_dict)

generate_cubes_dictionary()
