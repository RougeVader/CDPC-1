number = int(input("Enter a number: "))

no = number
rev = 0

while no > 0:
    rem = no % 10
    rev = rev * 10 + rem
    no = no // 10

if number == rev:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")