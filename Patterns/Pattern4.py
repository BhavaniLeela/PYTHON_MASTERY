rows = 5
for i in range(rows,0,-1):
    for j in range(0, i+1):
        print(j, end = " ")
    print("\r")

#By using generator function
rows = 5
for i in range(rows, 0, -1):
    print(" ".join(str(j) for j in range(i+1)))



rows = 6
for row in range(1, rows):
    for column in range(row, 0, -1):
        print(column, end = " ")
    print(" ")

"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""