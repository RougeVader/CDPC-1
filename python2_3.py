no=0
original_no = no
num_digits = len(str(no))
armstrong_sum = 0

while no > 0 and no<1000:
    rem = no % 10
    armstrong_sum = armstrong_sum + rem ** num_digits
    no = no // 10
    no=+1

if armstrong_sum == original_no:
    print("  an Armstrong number",no)
else:
    print("not an Armstrong number")