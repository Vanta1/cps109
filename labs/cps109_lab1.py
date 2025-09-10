### CPS109 Lab 1
# Cooper Sandys, 501347744

import math

### Question 1
temp = float(input("Enter a temperature in Celsius: ")) # using a float here b/c decimals and negatives are common when expressing temperature

f = (temp * (9.0 / 5.0)) + 32.0
k = temp + 273.15

print(f"The temperature entered is equal to {f} degrees Fahrenheit and {k} degrees Kelvin.") # i had to google f-strings, which seem identical to Rust's format! macro so this was more familiar

### Question 2
coefs_str = input("Input 3 comma-separated floats for a, b and c of a standard form polynomial: ").split(",")
coefs = [0.0] * 3

for x in range(0, 3):
    coefs[x] = float(coefs_str[x]) # using a float as polynomials can have negative and non-integer coefficients

discriminant = (coefs[1] ** 2) - (4 * coefs[0] * coefs[2])

if discriminant < 0:
    print("The function has no roots")
elif discriminant == 0:
    qf = (-coefs[1] + math.sqrt(discriminant)) / (2 * coefs[0])
    print(f"The function has a root at x = {qf}")
else:
    # qfp = quadratic formula using a plus sign, qfm = minus sign
    qfp = (-coefs[1] + math.sqrt(discriminant)) / (2 * coefs[0])
    qfm = (-coefs[1] - math.sqrt(discriminant)) / (2 * coefs[0])
    print(f"The roots of the polynomial described are x = {qfp} and x = {qfm}")

### Question 3
sides_str = input("Input 3 comma-separated side lengths of a triangle: ").split(",")
sides = [0.0] * 3

for x in range(0, 3):
    sides[x] = abs(float(sides_str[x])) # using a float for flexibility, and the absolute value to handle negative inputs

sides.sort() # sort the sides by length in ascending order to

print((sides[0] + sides[1]) > sides[2]) # if the 2 shortest side lengths combined are greater than the longest side, they can describe a triangle

### Question 4
sl = float(input("Enter the side length of a regular pentagon: ")) # using a float for flexibility

a = 0.25 * (math.sqrt(5 * (5+2*math.sqrt(5)))) * (sl ** 2)

print(f"The area of the pentagon is: {a}")

### Question 5
n = int(input("Enter a number 'n' for the nth number in the fibonacci sequence: ")) # int here is self explanatory

phi = (math.sqrt(5) + 1) / 2 # precalculating phi, like the question hinted
fn = (((2 + phi) / 5) * (phi ** n)) + (((3 - phi) / 5) * (phi ** (-n)))

print(f"The nth number of the fibonacci sequence is approximately: {fn}")

### Quiz 1
# args = input("Input the number of sides 'n' and the side length 'l' as comma-separated ints/floats respectively: ").split(",")
#
# n = int(args[0]) # there can only be a positive integer number of sides
# l = float(args[1]) # the side length could be any number
#
# apothem = l / (2 * math.tan((math.pi / n)))
# a = (apothem * (n * l)) / 2
#
# print(f"The area of the polygon described is: {a}")
