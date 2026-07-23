CurrentNumber = 1
stop = 2
rows = 3  #Rows you want in your pattern

for i in range(rows):
    for column in range(1, stop):
        print(CurrentNumber, end = " ")
        CurrentNumber += 1
    print(" ")
    stop += 2


CurrentNumber = 1
rows = 4       #Rows you want in your pattern.
stop = 2 

for i in range(rows):
    for column in range(1, stop):
        print(CurrentNumber, end = " ")
        CurrentNumber += 1
    print(" ")
    stop += 1