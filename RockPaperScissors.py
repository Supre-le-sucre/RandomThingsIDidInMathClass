from random import randint
round = 1
string = ""
player_point = 0
cpu_point = 0
choice = 0
Unplayable = True
c = "y"
while(c == "y"):
    print("===========")
    if(cpu_point < 3 and player_point < 3):
        Unplayable = True
        while(Unplayable):
            choice = input("Round %s \n1- Rock \n2- Paper\n3- Scissors\n" % round)
            if not choice.isnumeric():
                print("Please provide a valid option !")
            else:
                choice = int(choice)
                if(choice>3 or choice<=0):
                    print("Please provide a valid option !")
                else:
                    Unplayable = False
        if(choice == 1): string = "rock"
        if(choice == 2): string = "paper"
        if(choice == 3): string = "scissors"
        print("You: "+string.upper()+" !!")
        CPU = randint(1,3)
        if(CPU == 1):
            print("CPU: ROCK !!")
            if(CPU == choice):
                print("Tie !")
                round += 1
            if(choice == 3):
                print("CPU won !")
                cpu_point += 1
                round +=1
            if(choice == 2):
                print("Player won !")
                player_point += 1
                round += 1
        if(CPU == 2):
            print("CPU: PAPER !!")
            if(CPU == choice):
                print("Tie !")
                round += 1
            if(choice == 1):
                print("CPU won !")
                cpu_point += 1
                round +=1
            if(choice == 3):
                print("Player won !")
                player_point += 1
                round += 1
        if(CPU == 3):
            print("CPU: SCISSORS !!")
            if(CPU == choice):
                print("Tie !")
                round += 1
            if(choice == 2):
                print("CPU won !")
                cpu_point += 1
                round +=1
            if(choice == 1):
                print("Player won !")
                player_point += 1
                round += 1
    else:
        if(cpu_point == 3): print("CPU won the game !")
        if(player_point == 3): print("Player won the game !")
        c = input("Revenge ? (y/n)\n")
        if(c == "y"):
            round = 1
            string = ""
            player_point = 0
            cpu_point = 0
            c = "y"
print("See you next time !")
