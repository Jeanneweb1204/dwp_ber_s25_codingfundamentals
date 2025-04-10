def greet(first_name , second_name):
    print("Hello ," + first_name + " " + second_name + " are you ready for some fun coding today?")

greet("Alice","Smith")

print("# solution 2")
def repeat_character(character, number= 4):
    print(character * number)
print(repeat_character("c"))


print(" # solution 3")
def repeat_character_3(character,number):
    if number > 10:
        print("Sorry,too long")
    else:
        print(character*number) 
repeat_character_3("m",50)
repeat_character_3("t",7)