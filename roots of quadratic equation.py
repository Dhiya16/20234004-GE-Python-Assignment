

import cmath

def find_roots(a, b, c):

    d = cmath.sqrt(b**2 - 4*a*c)


    root1 = (-b + d) / (2 * a)
    root2 = (-b - d) / (2 * a)

    return root1, root2

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


roots = find_roots(a, b, c)
print("Root 1:", roots[0])
print("Root 2:", roots[1])
