n = int(input())

for i in range(1, n+1):
    o = ""
    if i % 3 == 0:
        o += "Fizz"
    if i % 5 == 0:
        o += "Buzz"

    if o != "":
        print(o)
        continue

    print(i)
