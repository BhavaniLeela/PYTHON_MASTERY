#Fibonacci is a series of numbers where each number is a sum of previous two numbers
# 0 1 1 2 3 5 8 13....

num=int(input("Enter a number:"))
a,b=0,1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b