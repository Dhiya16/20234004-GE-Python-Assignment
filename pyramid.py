

def print_pyramid(rows):
    for i in range(1, rows + 1):

        print(" " * (rows - i), end="")

        print("* " * i)

def print_reverse_pyramid(rows):
    for i in range(rows, 0, -1):

        print(" " * (rows - i), end="")

        print("* " * i)


num_rows = int(input("Enter the number of rows for the pyramid: "))


print("Pyramid:")
print_pyramid(num_rows)


print("Reverse Pyramid:")
print_reverse_pyramid(num_rows)
