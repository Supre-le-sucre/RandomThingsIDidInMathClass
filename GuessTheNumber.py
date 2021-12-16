import time
from random import randint
again = "y"
while(again == "y"):
    endTime = time.monotonic()+30
    number = randint(0,1000)
    print("You have 30 seconds to guess \nthe number I picked ! \n=========\nIt's between 1 and 1000 included !")
    guessed = False
    tries = 0
    while ((time.monotonic() < endTime) and not guessed):
        print("=-=-=-=")
        guess = int(input("Make a guess !"))
        if guess < number:
            print("Higher ! /\\")
            tries+=1
        if guess > number:
            print("Lower ! \/")
            tries += 1
        if guess == number:
            tries += 1
            guessed = True
    print("---------------")
    if guessed == True:
        print("Congrats ! \nYou guessed the number in:\n"+ str(tries) +" tries\nAnd "+ str(int(30-(endTime - time.monotonic())))+"/30 seconds")
    else:
        print("Too bad ! The number was %s" %number)
        print("You tried to guess it %s times" %tries)
    again = input("Want to play again ? (y/n)")
print("See You next time !")


