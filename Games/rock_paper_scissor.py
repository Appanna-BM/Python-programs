import random
while True:
    choices = ["rock","paper", "scissor"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock , paper, or scissor ?:").lower()
    if player == computer:
        print("Computer :", computer)
        print("Player :", player)
        print("Its a tie")
    elif player == "rock":
        if computer == "paper":
            print("Computer :", computer)
            print("Player :", player)
            print("You lose")
        if computer == "scissor":
            print("Computer :", computer)
            print("Player :", player)
            print("You win")
    elif player == "scissor":
        if computer == "rock":
            print("Computer :", computer)
            print("Player :", player)
            print("You lose")
        if computer == "paper":
            print("Computer :", computer)
            print("Player :", player)
            print("You win")
    elif player == "paper":
        if computer == "scissor":
            print("Computer :", computer)
            print("Player :", player)
            print("You lose")
        if computer == "rock":
            print("Computer :", computer)
            print("Player :", player)
            print("You win")
    play_again=input("Play again ? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")

