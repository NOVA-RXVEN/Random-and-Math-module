import random

options = ["Rock", "Scissors", "Paper"]

playing = True
score = 0

while playing:
    comp_choice = random.choice(options)
    
    user_choice= input("Please choose Rock, Paper, Scissors (Ensure the spelling is the same): ")
    
    print(f"You chose:{user_choice}")
    print(f"You chose:{comp_choice}")
    
    if score < 5:
        if user_choice == comp_choice:
            print("It is a Tie!")
            print(f"Score: {score}\n\n")
            
        elif user_choice == "Rock" and comp_choice == "Scissors":
            print("Rock smashes Scissors. You Win!")
            score = score + 1
            print(f"Score: {score}\n\n")
            
        elif user_choice == "Paper" and comp_choice == "Rock":
            print("Paper covers Rock. You Win!")
            score = score + 1
            print(f"Score: {score}\n\n")
            
        elif user_choice == "Scissors" and comp_choice == "Paper":
            print("Scissors cut Paper. You Win!")
            score = score + 1
            print(f"Score: {score}\n\n")
            
        else: 
            print("You Lose, Computer wins this turn")
            print(f"Score: {score}\n\n")
            
    else:
        print(f"Player Wins! Score: {score}")
        playing = False