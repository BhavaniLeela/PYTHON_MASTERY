rows=6
b=0
for i in range(rows,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end=" ")
    print("\r")
    
#or we can also simply write like this

rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

#we can also write this by using generaor expression
rows = 5
for i in range(rows, 0, -1):
    print(" ".join(str(i) for _ in range(i)))

#first it generates numbers and joins it like 5 5 5 5 5
# _ we used this here for loop iterations not for the value of loop variable

rows = 5
for i in range(rows, 0, -1):
    num = i
    for j in range(0,i):
        print(num, end = " ")
    print("\r")