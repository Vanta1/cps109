#print() example
x = 8
print(x)
x_str = str(x)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)


# ------------------------------------------
# Write a program to say whether an integer x is even or odd
# and finish by printing 'all done'
# ------------------------------------------
x = int(input('A number: '))
if x % 2 == 0 :
    print(x, 'is even')
else :
    print(x, 'is odd')
print('all done')


# multi-way decision example
# x = 0, 5, 20
x = 0
if x < 2 :
    print("small")
elif x < 10 :
    print('Medium')
else :
    print("LARGE")
print('All done')


# ----------------------------------------------------------
# Write a program of nested if statements
# that reports how divisible x is by 2 and 3
#------------------------------------------
x = int(input("enter an integer: "))
if x % 2 == 0 :
    if x % 3 == 0 :
        print(x, 'is divisible by both 2 and 3')
    else :
        print(x, 'is divisible by only 2')
elif x % 3 == 0 :
    print(x, 'is divisible by only 3')
else :
    print(x, 'is not divisible by either 2 or 3')


# while loop example

command = ""

while command.lower() != "quit":
    print(command)
    command = input("Type 'quit' to stop: ")

print("Loop ended.")


# Guess a number game
secret = 7
guess = None

while guess != secret:
    guess = int(input("Guess the number (1–10): "))

print("Correct! The number was", secret)



# ----------------------------------------------------------
# Breaking out of  a loop
#------------------------------------------
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')


# ----------------------------------------------------------
# Finishing an iteration with continue
#------------------------------------------
while True:
    line = input('Please input sth > ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')


# ----------------------------------------------------------
# A Definite Loop with Strings
#------------------------------------------
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
   print('Happy New Year:', friend)
print('Done!')


# ----------------------------------------------------------
# for Loop examples
#------------------------------------------
mysum = 0
for i in range(7, 10):
    print('i = ', i)
    mysum += i
print("The sum is:", mysum)

mysum = 0
for i in range(5, 11, 2):
    print('i = ', i)
    mysum += i
print("The sum is:", mysum)


#--------------------------------------------------------
# program to display student's marks from record
#------------------------------------------
student_name = 'Jules'
marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')


for i in range(1, 4):
    for j in range(1, 4):
        print(i, 'x', j, '=', i*j)
