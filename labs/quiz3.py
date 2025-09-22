import re

p1 = input("enter new password: ")
p2 = input("re-enter new password: ")

if p1 != p2:
    print("Passwords must match")
    exit()

if len(p1) >= 8 and p1.lower() != p1 and p1.upper() != p1 and re.search('[0-9]', p1) != None:
    print('Password accepted.')
    exit()

print('Password must be 8 characters or longer and have at least one lowercase character, one uppercase character and one digit.')
