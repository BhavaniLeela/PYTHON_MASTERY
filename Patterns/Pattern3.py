num=int(input("Enter a number:"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(num,end=" ")
    print("\r")

#By using generator expression
num=5
for i in range(num,0,-1):
    print(" ".join(str(num) for _ in range(i)))