import math

args = input("Input the number of sides 'n' and the side length 'l' as comma-separated ints/floats respectively: ").split(",")
n = int(args[0]) # there can only be a positive integer number of sides
l = float(args[1]) # the side length could be any number
apothem = l / (2 * math.tan((math.pi / n)))
a = (apothem * (n * l)) / 2
print(f"The area of the polygon described is {a}")
