''' Simple ATM functionality simulation in Python.

* Assign "PIN" pre-declared in a variable.
* Allow user to enter 4 digit PIN - Attempts not more than 3 times.
* Assign "Savings" and other details pre-declared in a variable.
* Allow user to enter an number between 25 - 75 - If entered, allow user to press "Yes".
If the user unables to enter the number, the step gets broken and the user is asked to re-enter card.
* User is asked to choose an option among 4 options - Check balance, Withdraw, Deposite, Mini Statement
* Various funtions are called accordingly.
* Code written in functional approach to maintain DRY.
'''

def facility(): #    This block contains ATM functionality
    print("\n>> Hi {}. Please select your purpose.\n".format(userDetail()[2]))
    print("1. Check balance\n2. Withdraw\n3. Deposite\n4. Mini Statement\n")
    option = int(input(">> Please enter your option number: "))
    if (option == 1): #    Check balance part
        print("\n>> You chose to check balance.")
        print("\n>> Your balance is Rs. {}\n".format(str(userDetail()[3])))
        goodbyeNote()
    elif (option == 2): #    Withdraw part
        print("\n>> You chose to withdraw cash-note.\n")
        j = 0
        while (j < 4):
            moneyEntry = int(input(">> Please enter your amount in Rs. 200, Rs. 500 and Rs. 2000: "))
            if (moneyEntry % 200 == 0 or moneyEntry % 500 == 0 or moneyEntry % 2000 == 0):
                balance = withdraw(moneyEntry)
                t = 0
                while (t < 100000000):
                    t += 1
                print("\a\n.... Cash collection tray opens ....\a\n")
                print(">> Please collect your cash-note.")
                p = 0
                while (p < 100000000):
                    p += 1
                print("\a\n.... Cash collection tray closes ....\a\n")
                q = 0
                while (q < 100000000):
                    q += 1
                print(">> Your current balance is Rs. {}.\n".format(str(balance)))
                goodbyeNote()
                break
            else:
                j += 1
                print("\n>> Uanble to process your input amount type. Please re-enter your amount.")
                print("\n>> You have {} attemps left\n".format(str(3 - j)))
                if (j == 3):
                    sorryNote()
                    break
    elif (option == 3): #    Deposite part
        print("\n>> You chose to deposite cash-note.\n")
        deposite()
    elif (option == 4): #    Mini Statement part
        print("\n>> You chose to print Mini Statement.\n")
        print("***************************************************\nMINI STATEMENT:\n")
        print("Your balance is Rs. {}.\n".format(str(userDetail()[3])))
        print("Maze Bank - Los Santos has stopped printing papers.\n") 
        print("Dear user, please save trees and save lives.\n")
        print("***************************************************\n")
        goodbyeNote()
    else:
        print("\n>> Dear user, you have entered wrong input. Please retry again.\n")
        sorryNote()

def deposite(): #    This block contains deposite mechanism
    k = 0
    while (k < 4):
        print(">> Please deposite cash-note in Rs. 200, Rs. 500 and Rs. 2000.\n")
        amt = int(input(">> Enter amount you want to deposite: "))
        if (amt % 200 == 0 or amt % 500 == 0 or amt % 2000 == 0):
            print("\a\n.... Cash collection tray opens ....\a\n")
            presentMoney = userDetail()[3]
            r = 0
            while (r < 1000000):
                r += 1
            print(">> Please place your cash-note one by one.\n")
            x = 0
            while (x < 100000000):
                x += 1
            print("\a\n.... Cash collection tray closes ....\a\n")
            print(">> Your current balance is Rs. {}\n".format(str(presentMoney + amt)))
            goodbyeNote()
            break
        else:
            k += 1
            print("\n>> Unable to detect cash-note type. Please re-enter cash-note.\n")
            if (k == 3):
                sorryNote()
                break

def withdraw(moneyEntry): #    This block contains withdrawl mechanism
    remainMoney = userDetail()[3]
    amt = moneyEntry
    remainMoney -= amt
    return remainMoney

def goodbyeNote(): #    This block contains the goodbye note after ATM has been used
    w, l = 0, 0
    while (w < 10000000):
        w += 1
    print(">> Please take out your card.")
    while (l < 100000000):
        l += 1
    print("\n>> Thank you for using Maze Bank - Los Santos. Please visit again.")

def sorryNote(): #    This block contains failure note
    print(">> Response time-out. Please visit your nearest bank branch for further detals.")
    y = 0
    print("\n>> Please take out your card.")
    while (y < 100000000):
        y += 1
    print("\n>> We are sorry to see you go. Please visit again!")
    
def userDetail(): #    This block contains user PIN and other details
    pinNo = "1234"
    savingsMoney = 10000000
    phNo = 9876543210
    cardName = "Michael"
    infoData = (pinNo, phNo, cardName, savingsMoney)
    return infoData

def cardAccess(): #    This block contains the card access mechanism which calls the facility mechanism
    i = 0
    while (i < 100000000):
        if (i == 100000000/2):
            print("\n....... Card detected .......\n")
        i += 1
    attemptCount = 0
    while (attemptCount < 4): 
        pin = input(">> Please enter PIN: ")
        if (pin == userDetail()[0]):
            randomNum = input("\n>> Please enter any number between 25 - 75: ")
            if (int(randomNum) >= 25 and int(randomNum) <= 75):
                facility()
                break
            else:
                print("\n>> Dear user, you have entered a wrong input.\n")
                sorryNote()
                break
        else:
            attemptCount += 1
            print("\n>> Dear user, please re-enter correct PIN.")
            print("\n>> You have {} attempts left.\n".format(3 - attemptCount))
            if (attemptCount == 3):
                print(">> You have extended attempt limit.\n")
                sorryNote()
                break
    
def welcome(): #    This block is the welcome block, it calls the Card accessing block
    print("\n*********************************")
    print("Welcome to MAZE BANK - Los Santos")
    print("*********************************\n")
    print(">> Dear user, please enter your card.")
    cardAccess()

def main():
    welcome()

if __name__ == "__main__": #    Main block
    main()

# Download code to run locally
