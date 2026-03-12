num = int(input("Enter a 6-digit number: "))

# Extract each digit
digit1 = num % 10
num = num // 10
digit2 = num % 10
num = num // 10
digit3 = num % 10
num = num // 10
digit4 = num % 10
num = num // 10
digit5 = num % 10
num = num // 10
digit6 = num % 10
  
# Sum all digits
res = digit1 + digit2 + digit3 + digit4 + digit5 + digit6
print("The sum of the digits is: ", res)