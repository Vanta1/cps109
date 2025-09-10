while True:
    x = float(input('sqrt of: '))

    y = x / 2.0

    while abs(y*y-x) > 1e-6:
        y = (y+x/y) / 2.0
        print(y)
