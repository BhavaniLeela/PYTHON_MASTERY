rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end = " ")   #Print Number
    
    #line after each row to display pattern correctly
    print(" ")

#we can also simplify this solution by using string repetition
rows=6
for num in range(1,rows):
    print((str(num)+" ")*num)