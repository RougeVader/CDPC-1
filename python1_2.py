no = int(input("Enter a number: "))
number = 0
rev = 0
sum1 = 0
while no > 0:
	rem = no % 10
	rev = rev * 10 + rem
	no = no // 10
	sum1 = sum1+ rem
	number = number + 1
print("The reverse of the number is:", rev, "and the number of digits is:", number)
print("The sum of the digits is:", sum1)
