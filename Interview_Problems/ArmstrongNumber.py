#Armstrong number is Sum of each digit raised to the power of the number of digits equals the original number
#153=1**3+5**3+3**3=1+125+27=153


num = int(input("Enter a number: "))

digits = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")