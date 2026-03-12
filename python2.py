
num = int(input("Enter a number: "))
original_num = num

print(f"Individual digits of {original_num}:")
digit_sum = 0

def factorial(n):
    for i in range(2, n + 1):
        result *= i
    return result

for digit in str(original_num):
    d = int(digit)
    fact = factorial(d)
    print(f"{d}! = {fact}")
    digit_sum += fact

print(f"\nSum of factorials: {digit_sum}")

if digit_sum == original_num:
    print(f"{original_num} is a Peterson number")
