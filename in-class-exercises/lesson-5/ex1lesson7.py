print("row1:1, 2, 3 , 4, 5")
print("row2:2, 4, 6, 8, 10")
print("row3:3, 6, 9, 12, 15")
print("row4:4, 8, 12, 16, 20")
print("row5:5, 10, 15, 20, 25")


print("💚 our code")
print("row 1: ", end="")
for column in range(1, 6):
    print(column*1,end="|")
print()
print("row 2: ", end="")
for column in range(1, 6):
    print(column*2,end="|")
print()
print("row 3: ", end="")
for column in range(1, 6):
    print(column*3,end="|")
print()

print("💚 nested loop")
for column in range(1, 6):
    for row in range(1, 6):
        print(column * row, end=" | ")
print()