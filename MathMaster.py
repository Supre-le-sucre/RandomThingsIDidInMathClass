import time
from random import randint

def game():
    playAgain = "y"
    while(playAgain == "y"):
        points = 0
        total = 0
        print("In this game, you will have to complete a simple arithmetic equation between 2 numbers (each number are between 1 and 9 included) as fast as possible !")
        print("Select a gamemode, it will determine what you will ask to complete in  the equation !")
        choice = makeChoice()
        print("Gamemode set to %s" %choice)
        wantedTime = makeTime()
        print("Your timebank has been set to %s seconds, good Luck !\n======" %wantedTime)

        if(choice == 1):

            input("Type any key to begin !")
            endTime = time.monotonic() + wantedTime
            while(time.monotonic() < endTime):
                points += gamemode(1)
                total += 1
            print("=-RESULT-=\nIn gamemode 1 You scored " + str(points)+"/"+ str(total) + " points in " + str(wantedTime) + " seconds ! Congrats !")

        if(choice == 2):

            print("In this gamemode, operations only are +, - or *")
            input("Type any key to begin !")
            endTime = time.monotonic() + wantedTime
            while(time.monotonic() < endTime):
                points += gamemode(2)
                total += 1
            print("=-RESULT-=\nIn gamemode 2 You scored " + str(points)+"/"+ str(total) + " points in " + str(wantedTime) + " seconds ! Congrats !")

        elif(choice == 3):

            print("In this gamemode, answers must be between 1 and 9 included")
            input("Type any key to begin !")
            endTime = time.monotonic() + wantedTime
            while(time.monotonic() < endTime):
                points += gamemode(3)
                total += 1
            print("=-RESULT-=\nIn gamemode 3 You scored " + str(points)+"/"+ str(total) + " points in " + str(wantedTime) + " seconds ! Congrats !")

        elif(choice == 4):

            print("In this gamemode, you must provide the valid operation\n"
                  "in order to get to the answer\n"
                  "-operations only are +, - or *\n"
                  "-numbers must be between 1 and 9 included\n")

            input("Type any key to begin !")
            endTime = time.monotonic() + wantedTime
            while(time.monotonic() < endTime):
                points += gamemode(4)
            print("=-RESULT-=\nIn gamemode 4 You scored " + str(points)+"/"+ str(total) + " points in " + str(wantedTime) + " seconds ! Congrats !")

        elif(choice == 5):

            print("In this gamemode, you must provide a valid operation\n"
                  "BETWEEN 2 NUMBERS !\n"
                  "in order to get to the answer\n"
                  "-operations only are +, - or *\n"
                  "-numbers must be between 1 and 9 included\n")

            input("Type any key to begin !")
            endTime = time.monotonic() + wantedTime
            while(time.monotonic() < endTime):
                points += gamemode(5)
                total += 1
            print("=-RESULT-=\nIn gamemode 5 You scored " + str(points)+"/"+ str(total) + " points in " + str(wantedTime) + " seconds ! Congrats !")


        elif(choice == 6):

            mix = input("Wich gamemodes do you want to mix together ?\n"
                        "You can mix all gamemodes together if you want !\n"
                        "Type the gamemodes you want to mix like the example:\n"
                        "123 (Will mix gamemode 1, 2 and 3)\n")


            while (len(mix) == 1 or not(isNumeral(mix)) or not containsNotTheSameChr(mix)):
                print("\n----\nPlease provide a valid mix\n----")
                mix = input("Wich gamemodes do you want to mix together ?\n"
                            "You can mix all gamemodes together if you want !\n"
                            "Type the gamemodes you want to mix like the example:\n"
                            "123 (Will mix gamemode 1, 2 and 3)\n")


            hasGamemode1 = False
            hasGamemode2 = False
            hasGamemode3 = False
            hasGamemode4 = False
            hasGamemode5 = False

            for k in range(len(mix)):

                if not (hasGamemode1): hasGamemode1 = mix[k] == "1"
                if not (hasGamemode2): hasGamemode2 = mix[k] == "2"
                if not (hasGamemode3): hasGamemode3 = mix[k] == "3"
                if not (hasGamemode4): hasGamemode4 = mix[k] == "4"
                if not (hasGamemode5): hasGamemode5 = mix[k] == "5"

            gamemodesSelected = []

            if (hasGamemode1): gamemodesSelected.append(1)
            if (hasGamemode2): gamemodesSelected.append(2)
            if (hasGamemode3): gamemodesSelected.append(3)
            if (hasGamemode4): gamemodesSelected.append(4)
            if (hasGamemode5): gamemodesSelected.append(5)

            while (len(gamemodesSelected)<=1):
                print("\n----\nPlease provide a valid mix\n----")
                mix = input("Wich gamemodes do you want to mix together ?\n"
                            "You can mix all gamemodes together if you want !\n"
                            "Type the gamemodes you want to mix like the example:\n"
                            "123 (Will mix gamemode 1, 2 and 3)\n")
                hasGamemode1 = False
                hasGamemode2 = False
                hasGamemode3 = False
                hasGamemode4 = False
                hasGamemode5 = False

                for k in range(len(mix)):

                    if not (hasGamemode1): hasGamemode1 = mix[k] == "1"
                    if not (hasGamemode2): hasGamemode2 = mix[k] == "2"
                    if not (hasGamemode3): hasGamemode3 = mix[k] == "3"
                    if not (hasGamemode4): hasGamemode4 = mix[k] == "4"
                    if not (hasGamemode5): hasGamemode5 = mix[k] == "5"

                gamemodesSelected = []

                if (hasGamemode1): gamemodesSelected.append(1)
                if (hasGamemode2): gamemodesSelected.append(2)
                if (hasGamemode3): gamemodesSelected.append(3)
                if (hasGamemode4): gamemodesSelected.append(4)
                if (hasGamemode5): gamemodesSelected.append(5)

            announcement = "Okay ! You have selected gamemodes "
            for k in range(len(gamemodesSelected)):
                announcement += str(gamemodesSelected[k]) + " "
                if(k == len(gamemodesSelected)-2):
                    announcement+="and "

            print(announcement+"\nGood Luck !")
            input("Type any key to begin !")
            endTime = time.monotonic() + wantedTime
            while(time.monotonic() < endTime):
                selection = randint(0,len(gamemodesSelected)-1)
                points += gamemode(gamemodesSelected[selection])
                total += 1

            mixOf=""
            for k in range(len(gamemodesSelected)):
                if(k == len(gamemodesSelected)-1):
                    mixOf+="and "+str(gamemodesSelected[k])
                    break
                mixOf += str(gamemodesSelected[k]) + " "
            print("=-RESULT-=\nIn gamemode 6 (Mix of "+mixOf+") You scored " + str(points)+"/"+ str(total) + " points in " + str(wantedTime) + " seconds ! Congrats !\n=-=-=")
        playAgain = input("Want to play again ? (y/n)\n")
    print("See you next time !")






def isNumeral(str, canBeNegative = False):
    # this function does not exist in my calculator so I had to make my own
    isNumeral = True
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for k in range(len(str)):
        if (isNumeral == False):
            break
            # To avoid unnecessary memory consuming, check is stopped as soon as a letter has been detected
        if(len(str) > 1 and canBeNegative and k == 0):
            letterChecked = str[k+1]
        else:
            letterChecked = str[k]
        for j in range(len(numbers)):
            if (letterChecked == numbers[j]):
                break
                # The letterChecked match the number checked so we need to break
            elif (j < len(numbers) - 1):
                continue
                # The letterChecked is not the number that was scanned, but other numbers remained unchecked,
                # so we have to continue
            else:
                isNumeral = False
                # The letterChecked did not match any number in the list, so it's not a number, we have to break
                break
    return isNumeral

def containsNotTheSameChr(str):
    # We need to check if there is at least one different character in a string
    isSame = False
    chrCheck = str[0]
    for k in range(len(str)-1):
        isSame = chrCheck == str[k+1]
        if not isSame:
            # A different character has been detected, we can break
            break
    return not isSame

def makeChoice():
    invalid = True
    choice = 1
    while (invalid):
        choice = input("Select a Gamemode ! \n1- Answer\n2- Sign\n3- Number\n4- Both\n5- All Blank !\n6- Mix\n")
        if not (isNumeral(choice)):
            print("Choice must be a positive number \n=========")
        else:
            choice = int(choice)
            if (choice == 0 or choice > 6):
                print("Choice must between 1 and 6 included")
            else:
                invalid = False
    return choice


def makeTime():
    invalid = True
    Time = 10
    while (invalid):
        time = input("=========\nSet the duration of the game (in seconds)\n")
        if not (isNumeral(time)):
            print("Time must be a positive number")
        else:
            time = int(time)
            if (time < 10):
                print(":/ You are hoping to do well in less than 10 seconds ?\nPlease enter a valid duration !")
            elif (time > 60):
                print(":/ You are really ready to play more than 60 seconds ?\nPlease enter a valid duration !")
            else:
                invalid = False
    return time

def gamemode(gamemode):
    #returnTotal=True makes the function return always 1, to count how many operation has been given to the player
    point = 0
    a = randint(1, 9)
    b = randint(1, 9)
    operation = randint(1, 3)
    operation_string = ""
    result = 0
    if (operation == 1):
        operation_string = " + "
        result = a + b
    elif (operation == 2):
        operation_string = " - "
        result = a - b
    else:
        operation_string = " * "
        result = a * b
    if(gamemode == 1):
        answer = input(str(a) + operation_string + str(b) + " = ?\n")
        correct = False
        if(isNumeral(answer, True)):
            answer = int(answer)
            if(answer == result):
                correct = True

        if(correct):
            point += 1
            print("V Correct\n----")
        else:
            print("X Wrong\n----")
        return point

    if(gamemode == 2):
        answer = input(str(a) + " ? " + str(b) + " = " + str(result) + "\n")
        if(a == 2 and b == 2 and result == 4 and (answer =="+" or answer =="*")):
            point += 1
            print("V Correct\n----")
        elif ((answer != "+" and operation == 1) or (answer != "-" and operation == 2) or (answer != "*" and operation == 3)):
            print("X Wrong\n----")
        else:
            point += 1
            print("V Correct\n----")
        return point

    if(gamemode == 3):
        answer = input(str(a) + operation_string + "? = " + str(result) + "\n")
        correct = False
        if(isNumeral(answer)):
            answer = int(answer)
            if (answer == 0):
                print("0 is not valid !")
                correct = False
            elif(operation == 1):
                correct = a + answer == result
            elif (operation == 2):
                correct = a - answer == result
            elif (operation == 3):
                correct = a * answer == result

        if(correct):
            point += 1
            print("V Correct\n----")
        else:
            print("X Wrong\n----")
        return point

    if(gamemode == 4):
        answer = input(str(a)+" ? ? = " + str(result) + "\n")
        correct = False
        if(len(answer) == 2):

            if(isNumeral(answer[1])):
                number = int(answer[1])
                if(number == 0):
                    print("0 is not valid !")
                    correct = False
                elif(answer[0]=="+"):
                    correct = a + number == result
                elif(answer[0]=="-"):
                    correct = a - number == result
                elif(answer[0]=="*"):
                    correct = a * number == result

        if(correct):
            point += 1
            print("V Correct\n----")
        else:
            print("X Wrong\n----")
        return point

    if(gamemode == 5):
        answer = input("? ? ? = " + str(result) + "\n")
        correct = False
        if(len(answer) == 3):

            if(isNumeral(answer[0]) and isNumeral(answer[2])):
                number1 = int(answer[0])
                number2 = int(answer[2])
                if(number1 == 0 or number2 == 0):
                    print("0 is not valid !")
                    correct = False
                elif(answer[1]=="+"):
                    correct = number1 + number2 == result
                elif(answer[1]=="-"):
                    correct = number1 - number2 == result
                elif(answer[1]=="*"):
                    correct = number1 * number2 == result

        if(correct):
            point += 1
            print("V Correct\n----")
        else:
            print("X Wrong\n----")
        return point

game()
