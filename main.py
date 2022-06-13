from art import Art
import random
art=Art()

user_input=int(input("choose your fingers: \n 0: rock \n 1: paper \n 2: scissors \n "))
print(f"your choice is :{user_input}")
print(art.game_list[user_input])

computer_choice=random.randint(0,2)
print(f"computer choice is :{computer_choice}")
print(art.game_list[computer_choice])

if user_input>=3 or user_input<0:
    print("invalid")
elif user_input==0 and computer_choice==2:
    print("you win")
elif user_input==2 and computer_choice==0:
    print("you lose")
elif user_input> computer_choice:
    print("you win")
elif user_input< computer_choice:
    print("you lose")
