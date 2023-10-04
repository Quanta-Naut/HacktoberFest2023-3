import random


while True:
    comp_choice = random.randint(1, 3)

    result = "draw"

    print("1 -> Rock\n2 -> Paper\n3 -> Scissor")
    choice = int(input("Enter your choice :"))

    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please ☺"))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"

    if choice == 1 and comp_choice == 2:
        print("paper wins\n")
        result = "Paper"
    elif choice == 2 and comp_choice == 1:
        print("paper wins\n")
        result = "paper"

    if choice == 1 and comp_choice == 3:
        print("Rock wins\n")
        result = "Rock"
    elif choice == 3 and comp_choice == 1:
        print("Rock wins\n")
        result = "rock"

    if choice == 2 and comp_choice == 3:
        print("Scissors wins\n")
        result = "scissor"
    elif choice == 3 and comp_choice == 2:
        print("Scissors wins\n")
        result = "Scissor"

    if result == "draw":
        print("***** Tie *****")
    elif result == choice_name:
        print("***** User wins *****")
    elif result != choice_name:
        print("***** Computer wins *****")

    print("Do you want to play again? (Y/N)")

    ans = input().lower
    if ans == "n":
        break
print("Great playing!!")
