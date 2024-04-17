import random
def rock_paper_scissors():
    gesture = ["rock","paper","scissors"]
    computer_choice = random.choice(gesture)
    print("enter your choice:(rock,paper,scissors)")
    player_choice = input().lower()
    if player_choice not in gesture:
        print("invalid gesture,please try again:")
        rock_paper_scissors()
    print("computer choice:",computer_choice)
    if player_choice == computer_choice:
        print("its a tie")
    elif (player_choice == "rock" and computer_choice=="scissors") or (player_choice=="paper" and computer_choice=="rock") or (player_choice=="scissors" and computer_choice=="paper"):
        print("you win")
    else:
        print("you lose")
    play_again = input("do you want to play again (yes or no):").lower()
    if play_again=="yes":
        rock_paper_scissors()
    else:
        print("thank you for playing")
        exit()
print("Welcome to the game rock_paper_scissors")
rock_paper_scissors()
