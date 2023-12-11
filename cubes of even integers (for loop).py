

def cubes_of_even_numbers_for_loop(input_list):
    result = []
    for element in input_list:
        if isinstance(element, int) and element % 2 == 0:
            result.append(element**3)
    return result

input_list = [7,45,6,79,99]
result_for_loop = cubes_of_even_numbers_for_loop(input_list)
print("Result using 'for' loop:", result_for_loop)
