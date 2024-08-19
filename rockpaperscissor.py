import random

def rps():
    rock = "0"
    paper = "1"
    scissor = "2"
    print(rock," is rock")
    print(paper," is paper")
    print(scissor," is scissor")
    player = input("ENTER YOUR CHOICE\n")
    
    if player == rock:
        print(f"YOUR CHOICE IS ROCK")
    elif player == paper:
        print(f"YOUR CHOICE IS PAPER")
    elif player == scissor:
        print(f"YOUR CHOICE IS SCISSOR")
    else:
        print("INVALID CHOICE")
        exit()
    
    l = ["rock","paper","scissor"]
    computer = random.choice(l)
    print(f"Computer choice is {computer}")
    
    if player == rock and computer == "rock":
        print("it's an draw")
    elif player == paper and computer == "paper":
        print("it's an draw")
    elif player == scissor and computer == "scissor":
        print("it's an draw")
    
    if player == rock and computer == "scissor":
        print("player won")
    elif player == paper and computer == "rock":
        print("player won")
    elif player == scissor and computer == "paper":
        print("player won")

    if player == rock and computer == "paper":
        print("player lost")
    elif player == paper and computer == "scissor":
        print("player lost")
    elif player == scissor and computer == "rock":
        print("player lost")

if __name__ == '__main__':
    rps()
