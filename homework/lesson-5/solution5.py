print("## exercices 2")
def count_letter(word):
    counter=0
    for letter in word:
        if letter.isalpha() or letter.isnumeric():
            counter+=1
    print("The lenght of "+ word + " is " + str(counter))
count_letter("Forest")
count_letter("forest123")

print("## exercice4")
import random
def play_game(user_choice):
    possible_move=["rock" "paper","scissors"]
    computer_move=random.choice(possible_move)
    if computer_move == user_choice:
        print("it's tie!")
    elif computer_move=="rock":
        if user_choice== "paper":
            print("you win")
        else :
            print("you lose")
        if user_choice=="rock":
            print("you win")
        else:
            print("you lose")
    

print("Random exercices")
def is_even(number):
    return number % 2==0
l=[1,2,3,4,5]
for n in l:
    if not is_even(n):
        print(n)

print("## additional")
def t(number=input()):
    print("The number is " + number)
t()