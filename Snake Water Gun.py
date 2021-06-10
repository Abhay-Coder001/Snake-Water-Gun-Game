import random
SWG = ["Snake", "Water", "Gun"]
computer = random.choice(SWG)
player = False
i = 0
Pscr = 0
Cscr = 0
'''Player False rakha Kyon Ki Jab program run hoga tab 
status change hoke from False to True ho jayega 
kyon ki jab hi player ko koi value dunga uski status true ho jayegi'''
while (i<10):
    player = input("Snake, Water, Gun?")
    if player == computer:
        print("Tie!")
    elif player == "Snake":
        if computer == "Gun":
            print("You lose!", computer, "Maar Diya", player, "Ko.")
            Pscr = Pscr-1
            Cscr = Cscr+1
        else:
            print("You win!", player, "Bhag Gaya Swim Karke", computer, "Mein." )
            Pscr = Pscr + 1
            Cscr = Cscr - 1
    elif player == "Water":
        if computer == "Snake":
            print("You lose!", computer, "Bhag Gaya Swim Karke", player, "Mein." )
            Pscr = Pscr - 1
            Cscr = Cscr + 1
        else:
            print("You win!", player, "Duba Diya", computer, "Ko." )
            Pscr = Pscr + 1
            Cscr = Cscr - 1
    elif player == "Gun":
        if computer == "Water":
            print("You lose...", computer, "Bhigo Diya", player, "Ko.")
            Pscr = Pscr - 1
            Cscr = Cscr + 1
        else:
            print("You win!", player, "Maar Diya", computer, "Ko.")
            Pscr = Pscr + 1
            Cscr = Cscr - 1
    else:
        print("Check your spelling!")
    computer = random.choice(SWG)
    i= i+1
    if (i==10):
        print("Your Final Score Is")
        print(Pscr)
        print("And Computers Final Score Is")
        print(Cscr)
        if Pscr == Cscr:
            print("Match Drawn")
        elif Pscr>Cscr:
            print('You Win')
        else:
            print("You Lose")