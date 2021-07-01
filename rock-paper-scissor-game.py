''' ! Basic Rock-Paper-Scissor game written in Python 3.
    ! Usage of Functional programming paradigm.
    ! Game simulation type is User vs. Computer.
'''

import random

movesAvail = ("rock", "paper", "scissor") #     this is the moves tuple

def compChoice(): #     this is the computer random choosing block
    return random.choice(movesAvail)

def gameMessages(): #       this block is to print out game emotions
    msg1 = "\n=> Oopsie-topsie! A paper-cut XD XD\n"
    msg2 = "\n=> Yaay! You wrapped up a rock :D :D\n"
    msg3 = "\n=> Yaay! You paper-cut :D :D\n"
    msg4 = "\n=> Oopsie-topsie! Your rock got wrapped up XD XD\n"
    msg5 = "\n=> Oopsie-topsie! Your scissor got smashed down XD XD\n"
    msg6 = "\n=> Yaay! You smashed down a scissor :D :D\n"
    msg7 = "\n=> There's not point for equality here :P :P\n"
    return (msg1, msg2, msg3, msg4, msg5, msg6, msg7)

def resultWaitNote(): #     this block alerts user to wait for result
    print("=> Game over :/ :/\n")
    z = 0
    while (z < 100000000):
        if (z == 100000000//2):
            print(".... Waiting for results ....\n")
        z += 1

def delayer(): #    a simple delay time block
    y = 0
    while (y < 100000000):
        y += 1

def gameLogic(): #      this is the game logic and simulation block 
    userResp = ""
    compResp = ""
    counter = 1
    compPoint = userPoint = 0
    getOut = ""
    while (counter < 4): #      outer loop for counting 3 shakes
        if (getOut.lower() != "yes"): #     check if not yes then block executes
            userResp = input("<> Shake {}: Please enter your choice: ".format(str(counter)))
            if (userResp.lower() in movesAvail):
                compResp = compChoice()
                if (compResp == "scissor" and userResp.lower() == "paper"):
                    print(gameMessages()[0])
                    compPoint += 1 
                    counter += 1
                elif (compResp == "rock" and userResp.lower() == "paper"):
                    print(gameMessages()[1])
                    userPoint += 1
                    counter += 1
                elif (compResp == "paper" and userResp.lower() == "scissor"):
                    print(gameMessages()[2])
                    userPoint += 1
                    counter += 1
                elif (compResp == "paper" and userResp.lower() == "rock"):
                    print(gameMessages()[3])
                    userPoint += 1
                    counter += 1
                elif (compResp == "rock" and userResp.lower() == "scissor"):
                    print(gameMessages()[4])
                    compPoint += 1
                    counter += 1
                elif (compResp == "scissor" and userResp.lower() == "rock"):
                    print(gameMessages()[5])
                    userPoint += 1
                    counter += 1
                else:
                    print(gameMessages()[6])
            else:
                print("\n=> **warning** Invalid choice entered. Please enter correct shake move (rock, paper or scissor) X( X(\n")
                getOut = input("<> Please press <enter> to retry, else type <yes> to exit the game: ")
                print("\n")
                if (getOut.lower() == "yes"):
                    break
    if (getOut.lower() == "yes"):
        pass #      doing nothing
    else:
        return (compPoint, userPoint) #     returning values if it contains as such
  
def gameResult(userPts, compPts): #     this block prints the winner as per game points
    winner = ""
    if (userPts > compPts):
        winner = userPts
        print("=> Yaay! You have won by {} points ^_^ ^_^".format(str(userPts - compPts)))
    else:
        print("=> Ooopsie-topsie! You have lost by {} points *_* *_*".format(str(compPts - userPts)))
    
def set2(): #       block for Set of 2 mode
    delayer()
    counter = user = comp = 0
    while (counter < 3):
        try:
            userPts, compPts = gameLogic()
            user += userPts
            comp += compPts
            counter += 1
     #      follow gameResult() block
        except:
            break
    if (counter != 0):
        resultWaitNote() #      follow resultWaitNote() block
        gameResult(user, comp)

def set1(): #       block for Set of 1 mode
    delayer()
    try:
        userPts, compPts = gameLogic()
        resultWaitNote() #      follow resultWaitNote() block
        gameResult(userPts, compPts) #      follow gameResult() block
    except:
        pass

def set3(): #       block for Set of 3 mode
    delayer()
    counter = user = comp = 0
    while (counter < 4):
        try:
            userPts, compPts = gameLogic()
            user += userPts
            comp += compPts
            counter += 1
        except:
            break
    if (counter != 0):
        resultWaitNote() #      follow resultWaitNote() block
        gameResult(user, comp) #        follow gameResult() block
 
def gameMode(): #       this block is the interface for game, includes mode choices etc.
    delayer()
    print("1. Set of 1 (1 game 3 shakes => 1 * 3 shakes)\n2. Sets of 2 (2 games 3 shakes => 2 * 3 shakes)\n3. Sets of 3 (3 games 3 shakes => 3 * 3 shakes) \n")
    userInpAgain = ""
    while (userInpAgain.lower() != "quit"):
        gameChoice = input("<> Please enter the Set (option) you want to play: ")
        if (gameChoice == "1"):
            print("\n=> So you've chosen Set of 1 to play :)")
            print("\n=> Let's play the game :D :D\n")
            set1()
            break
        elif (gameChoice == "2"):
            print("\n=> So you've chosen Set of 2 to play :)")
            print("\n=> Let's play the game :D :D\n")
            set2()
            break
        elif (gameChoice == "3"):
            print("\n=> So you've chosen Set of 3 to play :)")
            print("\n=> Let's play the game :D :D\n")
            set3()
            break
        else:
            print("\n=> **warning** Invalid option entered. Please enter correct option number X( X(\n")
            userInpAgain = input("<> Please press <enter> to retry, else type <quit> to exit the game: ")
            print("\n")
    goodbyeNote() #     follow goodbyeNote() function block

def goodbyeNote(): #        this block throws goodbye message
    print("\n=> So sorry to see you go. Please play again ^_^ ^_^")

def welcomeNote(): #        this block throws welcome message 
    firstStrVar = "## Welcome to the famous old-school Rock-Paper-Scissor game ##" #        "firstStrVar" To be used for appending by length
    print("\n")
    print((len(firstStrVar)//4 * " ") + "@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print((len(firstStrVar)//4 * " ") + "@ Rock | Paper | Scissor @")
    print((len(firstStrVar)//4 * " ") + "@@@@@@@@@@@@@@@@@@@@@@@@@@\n" + "\n")
    print(firstStrVar)
    delayer()
    print("\n.............. Game loading in progress ..............")
    delayer()
    playerName = input("\n<> Hi user, please enter your name: ")
    delayer()
    print("\n=> Hey {}, welcome to this game. You will be playing against Mr. Robot :D :D\n".format(playerName))
    gameMode() #        follow gameMode() function block

if __name__ == "__main__":
    welcomeNote()
