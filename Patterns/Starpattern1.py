result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if row == 0 or row == 6 or row + column == 6:
            result_str += "*"
        else:
            result_str += " "
    result_str += "\n"
print(result_str)