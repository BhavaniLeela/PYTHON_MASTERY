#Palindrome number is a number which equals with the original number after reversing it
#Example:121=121

num=int(input("Enter a number:"))
original=num
reverse=0
while num:
    reverse=reverse*10+num%10
    num//=10
if original==reverse:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")

num = int(input("Enter a number: "))

original = num
reverse = 0

while num:
    reverse = reverse * 10 + num % 10
    num //= 10

if original == reverse:
    print(f"{original} is a Palindrome")
else:
    print(f"{original} is not a Palindrome")