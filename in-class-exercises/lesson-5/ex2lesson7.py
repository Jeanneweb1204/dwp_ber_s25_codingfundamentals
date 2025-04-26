
name = input("What's your name:")
print(f"💖 nested loop for {name}")
size = int(input("table size:")) +1
for column in range(1, size):
    print(f"row {column}: ", end="") # string interpolation 
    for row in range(1, size):
        if column * row <= 9:
            print(column * row, end="  | ")
        else:
            print(column * row, end=" | ")
    print()


    count = 1

while count <= 10:
    print("💖", count)
    count +=1


for count in range(0, 11):
    print("💚", count)
    count +=1