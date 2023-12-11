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

def swap_first_n_chars(str1, str2, n):
    if n <= 0:
        print("Please enter a positive value for n.")
        return

    if n > min(len(str1), len(str2)):
        print("Value of n exceeds the length of one or both strings.")
        return

    swapped_str1 = str2[:n] + str1[n:]
    swapped_str2 = str1[:n] + str2[n:]

    print("After swapping the first {n} characters:")
    print("String 1:" swapped_str1)
    print("String 2:" swapped_str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
n_value = int(input("Enter the value of n: "))

swap_first_n_chars(string1, string2, n_value)
