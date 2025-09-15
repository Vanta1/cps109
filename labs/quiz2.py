i = int(input("Enter an integer: "))
prime = True
for n in range(2,11):
    if i % n == 0:
        print(n)
        prime = False

if not prime:
    print("This number has no factors between 2 and 10.")
