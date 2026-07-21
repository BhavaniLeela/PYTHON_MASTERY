#Factorial is multiplication from 1 to N
#num=5
# 5!=5*4*3*2*1=120

num=int(input("Enter a number:"))
if num<0:
    print("Number cannot in negative value for factorial")
else:
    factorial=1
    for i in range(2,num+1):
        factorial*=i
    print(f"Factorial of {num} is {factorial}")