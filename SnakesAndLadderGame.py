#Created by Rudra Shah 11-B DIN
import random
import time

userSteps = 0 #initial Step is always 0
userSteps2 = 0

for space in range(0,10):
    False
for extra in range(0,2):
    print(" ")

def WelcomeMessage():
    print(" "*(space-6),"SNAKES AND LADDERS")
    print(" "*space,"Version 1.1")
    print(" "*space,"Created by-: Rudra shah")
    print(" "*space,"GitHub-: https://github.com/sciencelabwork")    

def helpMe():
    print(" "*(space-4),"#Rules of the Snakes and Ladders")
    print(" "*space,"1)This Game is played between Two players. Max. and Min. 2 players are required!")
    print(" "*space,"2)To roll a dice simple press \"ENTER\" Key, Don\'t Type ENTER!!")
    print(" "*space,"3)To know rules in between the game type \"HELP\".")
    print(" "*space,"4)If any bugs are found report it on GitHub or DM me on instagram(no missuse).")

def Exit():
    print(" "*(space-4),"SNAKES AND LADDERS")
    print(" "*space,"Created by-: Rudra shah")
    print(" "*space,"GitHub-: https://github.com/sciencelabwork")
    print(" "*space,"instagram-: https://www.instagram.com/rudra_shah_")

WelcomeMessage()
for extra in range(0,1):
    print(" ")
helpMe()
user1name = input("\nPlayer1 Name: ")
user2name = input("\nPlayer2 Name: ")

for RangeTime in range(0,101):
    time.sleep(0.1)
    if RangeTime==random.randint(0,101):
        time.sleep(7)
    print('Starting Snake AND Ladders---%d\r'%RangeTime,end="")

print("\nSo let\'s have a cheerful Match of Snakes And Ladders between \'%s\'"%user1name.upper(),"and","\'%s\'"%user2name.upper())

ladder = { #7LADDERS
    4:14, #14
    9:31, #31
    21:42, #42
    28:84, #84
    51:67, #67
    71:91, #91
    80:100 #100
}

snakes = { #8SNAKES
    17:7, #7
    54:34, #34
    62:19, #19
    64:60, #60
    87:24, #24
    93:73, #73
    95:75, #75
    98:79 #79
}

exitOutput = [
    'T',
    't',
    'Exit',
    'exit',
    'EXIT'
]

helpMeOut = [
    'help',
    'HELP',
    'H',
    'h'
]


try:
    while True:
        enterInput1 = input("\n%s It\'s your chance!!....Press \"ENTER\" to roll a dice"%user1name.upper())
        if enterInput1 == "":
            print("Rolling dice")
            for i in range(0,3):
                time.sleep(1)
            diceRolled = random.randint(1,6)
            print("You rolled it",diceRolled)
            oldStep = userSteps
            userSteps+=diceRolled
            if userSteps in ladder:
                oldStepLadder = userSteps
                userSteps=ladder[userSteps]
                print("OHH! you climb up the stairs from",oldStepLadder,"to",userSteps)
            elif userSteps in snakes:
                oldsnakeStep = userSteps
                userSteps=snakes[userSteps]
                print("You are eatten by a snake, You have climbed back to",userSteps,"from",oldsnakeStep)
            else:
                if userSteps>=100:
                    print(100)
                else:
                    print("you travelled from",oldStep,"to",userSteps)
            if userSteps>=100:
                print("\nGame over!! CONGRATULATIONS!!",user1name,"WON THE SNAKE & LADDER GAME")
                break
        elif enterInput1 in helpMeOut:
            helpMe()
        elif enterInput1 in exitOutput:
            print("\nBye")
            Exit()
            break
        else:
            print("Invalid Input")

        enterInput2 = input("\n%s It\'s your chance!!....Press \"ENTER\" to roll a dice"%user2name.upper())
        if enterInput2 == "":
            print("Rolling dice")
            for i in range(0,3):
                time.sleep(1)
            diceRolled = random.randint(1,6)
            print("You rolled it",diceRolled)
            oldStep2 = userSteps2
            userSteps2+=diceRolled
            if userSteps2 in ladder:
                oldStepLadder2 = userSteps2
                userSteps2=ladder[userSteps2]
                print("OHH! you climb up the stairs from",oldStepLadder2,"to",userSteps2)
            elif userSteps2 in snakes:
                oldsnakeStep2 = userSteps
                userSteps2-=snakes[userSteps2]
                print("You are eatten by a snake, You have climbed back to",userSteps2,"from",oldsnakeStep2)
            else:
                if userSteps2>=100:
                    print(100)
                else:
                    print("you travelled from",oldStep2,"to",userSteps2)
            if userSteps2>=100:
                print("\nGame over!! CONGRATULATIONS!!",user2name,"WON THE SNAKE & LADDER GAME")
                break
        elif enterInput1 in helpMeOut:
            helpMe()
        elif enterInput2 in exitOutput:
            print("\nBye")
            Exit()
            break 
        else:
            print("Invalid Input")
except:
    print("There was a error in the game")

