from datetime import datetime
def  current_date_time ():
    return datetime.today()
print("current date and time :" , current_date_time())

print("## Homework 2" )
input="izere"
count=0
for n in input:
    if n.isalpha():
        count=count+1

print("Number of the letters:",count)

print("## Homework 3")
def two_numbers(first_number,second_number):
    print(f"{first_number + second_number}")
two_numbers(4, 7)

def create_number(x):
    if x % 3==0 :
        print("Multiple of 3")
    else:
        print("No Multiple of 3")

create_number(18) 

print("## Homework 4")
from random import randint
def play_game(user_choice):
    choice=["Rock","Paper","Scissors"]
    computer_choice= random.randint(0,2)
    print(f"You chose:{choice[user_choice]}")
    print(f"Computer chose:{choice[computer_choice]}")

    if user_choice== computer_choice:
        return"Tie"
    elif (user_choice==0 and computer_choice==2)or(user_choice==1 and computer_choice==0)or (user_choice==2 and computer_choice==1):
        return"You win"
    else:
        return"You lose"
for i in range(3):
    print(f"\n --- Test with user choice: {i} ---")
    result = play_game(i)
    print("Result:", result)

