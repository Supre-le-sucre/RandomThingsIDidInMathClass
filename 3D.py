def main(debug=False):
    A = [0, 0, 0]
    B = [0, 0, 0]
    C = [0, 0, 0]
    D = [0, 0, 0]
    DIsDefine = False
    while True:
        user = input(">>> ")
        # ---------------------
        if user == "h":
            # Help command
            print("=-= Help =-= \na defines A etc. \npt returns defined points \npl returns a plan\ns stop the program")
        # ---------------------
        # ---------------------
        elif user == "s":
            print("To restart, use main()")
            return 0
        # ---------------------
        # ---------------------
        elif user == "a" or user == "b" or user == "c" or user == "d":
            coordinates = [0, 0, 0]
            if user == "a":
                Invalid = True
                while Invalid:
                    coordinatesNotFormated = input("Provide coordinates: x,y,z\nc to cancel\n")
                    if coordinatesNotFormated == "c":
                        coordinates = (str(A[0]), str(A[1]), str(A[2]))
                        Invalid = False
                    else:
                        coordinates = coordinatesNotFormated.split(",")
                    if len(coordinates) != 3:
                        Invalid = True
                    else:
                        Invalid = False
                for n in range(3):
                    if isNumeral(coordinates[n]):
                        A[n] = int(coordinates[n])
                    else:
                        A[n] = 0

            if user == "b":
                Invalid = True
                while Invalid:
                    coordinatesNotFormated = input("Provide coordinates: x,y,z\nc to cancel\n")
                    if coordinatesNotFormated == "c":
                        coordinates = (str(B[0]), str(B[1]), str(B[2]))
                        Invalid = False
                    else:
                        coordinates = coordinatesNotFormated.split(",")
                        if len(coordinates) != 3:
                            Invalid = True
                        else:
                            Invalid = False
                for n in range(3):
                    if isNumeral(coordinates[n]):
                        B[n] = int(coordinates[n])
                    else:
                        B[n] = 0

            if user == "c":
                Invalid = True
                while Invalid:
                    coordinatesNotFormated = input("Provide coordinates: x,y,z\nc to cancel\n")
                    if coordinatesNotFormated == "c":
                        coordinates = (str(C[0]), str(C[1]), str(C[2]))
                        Invalid = False
                    else:
                        coordinates = coordinatesNotFormated.split(",")
                        if len(coordinates) != 3:
                            Invalid = True
                        else:
                            Invalid = False
                for n in range(3):
                    if isNumeral(coordinates[n]):
                        C[n] = int(coordinates[n])
                    else:
                        C[n] = 0

            if user == "d":
                Invalid = True
                while Invalid:
                    coordinatesNotFormated = input("Provide coordinates: x,y,z\nc to cancel\n")
                    if coordinatesNotFormated == "c":
                        coordinates = (str(D)[0], str(D)[1], str(D)[2])
                        Invalid = False
                    else:
                        coordinates = coordinatesNotFormated.split(",")
                        if len(coordinates) != 3:
                            Invalid = True
                        else:
                            Invalid = False
                for n in range(3):
                    DIsDefine = True
                    if isNumeral(coordinates[n]):
                        D[n] = int(coordinates[n])
                    else:
                        D[n] = 0

        # ---------------------
        # ---------------------
        elif user == "pt":
            # Return points coordinates
            coordinatesFormat("A", A)
            coordinatesFormat("B", B)
            coordinatesFormat("C", C)
            if DIsDefine:
                coordinatesFormat("D", D)
        # ---------------------
        # ---------------------
        elif user == "pl":
            # Return system and cartesian equation of plan
            u = vectorCalc(A, B)
            v = vectorCalc(A, C)
            thereIsAPlan = True
            k = 1
            if v[0] == 0 or v[1] == 0 or v[2] == 0 and (u[0] != 0 and u[1] != 0 and u[2] != 0):
                thereIsAPlan = True
            for n in range(3):
                if v[n] != 0:
                    k = u[n] / v[n]
                    break
            if v[1] * k == u[1] and v[2] * k == u[2]:
                # Check if there is a coefficient between u and v
                thereIsAPlan = False

            if thereIsAPlan:
                system = " | x = "
                for n in range(3):
                    UIsAlreadyProcessed = False
                    VIsAlreadyProcessed = False
                    # Construction of system
                    if n == 1:
                        system += "<| y = "
                    elif n == 2:
                        system += " | z = "
                    if A[n] == 0 and (u[n] == 0 and v[n] == 0):
                        # Value of A is 0 and must be shown because other value are multiplied by 0
                        system += "0"
                    elif A[n] != 0:
                        # Value of A is not 0 and therefore has to be shown
                        system += str(A[n])
                    else:
                        # Value of A is 0 and should not be shown, program should format the text adequately
                        if u[n] == 0:
                            # Value of first coefficient is 0 and therefore should not be shown. Value of next
                            # coefficient should be different from 0 because this has been tested previously
                            UIsAlreadyProcessed = True
                            VIsAlreadyProcessed = True
                            if v[n] == 1:
                                system += "k'"
                            elif v[n] == -1:
                                system += "-k'"
                            else:
                                system += str(v[n]) + "k'"
                        else:
                            UIsAlreadyProcessed = True
                            if u[n] == 1:
                                system += "k"
                            elif u[n] == -1:
                                system += "-k"
                            else:
                                system += str(u[n]) + "k"
                    if not UIsAlreadyProcessed:
                        if u[n] > 0:
                            if u[n] == 1:
                                system += " + k"
                            else:
                                system += " + " + str(u[n]) + "k"
                        elif u[n] < 0:
                            if u[n] == -1:
                                system += " - k"
                            else:
                                system += " - " + str(abs(u[n])) + "k"
                    if not VIsAlreadyProcessed:
                        if v[n] > 0:
                            if v[n] == 1:
                                system += " + k'"
                            else:
                                system += " + " + str(v[n]) + "k'"
                        elif v[n] < 0:
                            if v[n] == -1:
                                system += " - k'"
                            else:
                                system += " - " + str(abs(v[n])) + "k'"
                    system += "\n"
                print(system)

                cartesianEquation = ""
                vectorN = normalVector(u, v)
                if debug : print("Normal vector is " + str(vectorN))

                d = 0
                for i in range(3):
                    if vectorN[i] != 0:

                        # This calculates the d at the end of the cartesian equation
                        d -= vectorN[i] + A[i]
                        if debug: print("Value of d is " + str(d))
                        commonDivisor = gcd([vectorN[0], vectorN[1], vectorN[2], d])
                        if i == 0:
                            cartesianEquation += str(int(vectorN[i]/commonDivisor)) + "x"
                        if i == 1:
                            if not cartesianEquation == "":
                                if vectorN[i] > 0:
                                    cartesianEquation += " + " + str(int(vectorN[i]/commonDivisor)) + "y"
                                else:
                                    cartesianEquation += " - " + str(abs(int(vectorN[i]/commonDivisor))) + "y"
                            else:
                                cartesianEquation += str(int(vectorN[i]/commonDivisor)) + "y"
                        if i == 2:
                            if not cartesianEquation == "":
                                if vectorN[i] > 0:
                                    cartesianEquation += " + " + str(int(vectorN[i]/commonDivisor)) + "z"
                                else:
                                    cartesianEquation += " - " + str(abs(int(vectorN[i]/commonDivisor))) + "z"
                            else:
                                cartesianEquation += str(int(vectorN[i]/commonDivisor)) + "z"

                if d > 0:
                    cartesianEquation += " + " + str(int(d/commonDivisor))
                elif d < 0:
                    cartesianEquation += " - " + str(abs(int(d/commonDivisor)))

                cartesianEquation += " = 0"
                print(cartesianEquation + "\n")

                if DIsDefine:
                    if isPointCoplanar(A, vectorN, D):
                        print("D is coplanar with P")
                    else:
                        print("D isn't coplanar with P")

            else:
                # There is no equation of plan to display because vectors are collinear
                print("Nothing to see here :/")
        else:
            print("Command not found\ntype h to see commands")


def coordinatesFormat(name, coordinates):
    # Returns correct formate for a point
    print(name + "(" + str(coordinates[0]) + ";" + str(coordinates[1]) + ";" + str(coordinates[2]) + ")")
    return 0


def vectorCalc(a, b):
    # Return coordinates of a vector give coordinates of 2 points
    return [b[0] - a[0], b[1] - a[1], b[2] - a[2]]


def normalVector(u, v):
    # Return coordinates of a normal vector given coordinates of two other vectors
    x, xp = u[0], v[0]
    y, yp = u[1], v[1]
    z, zp = u[2], v[2]
    return [(y * zp - yp * z), (z * xp - zp * x), (x * yp - y * xp)]


def isNumeral(str):
    # Check if a str is a number
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if '-' in str and len(str) > 1:
        # If str contains - remove minus before testing. We could have added the minus in the number table,
        # but this could cause the symbol minus to be considered a number and therefore returns an errors when cast
        # as an integer
        str = str[1:len(str)]
    for n in range(len(str)):
        if not str[n] in numbers:
            return False
    return True

def isPointCoplanar(A,n,D):
    # Given a point a and a normal vector n to create a cartesian equation, return if point d solve the cartesian
    # equation
    x = D[0]
    y = D[1]
    z = D[2]

    a = n[0]
    b = n[1]
    c = n[2]

    d = -a*A[0]-b*A[1]-c*A[2]

    return a*x+b*y+c*z+d == 0

def gcd(args):
    if len(args) <= 1:
        return 0
    min = abs(args[0])
    for n in range (len(args)):
        args[n] = abs(args[n])
        if args[n] < min:
            min = args[n]
    commonCoef = [1]
    for i in range(1,min+1):
        occur = 0
        # We clear the variable of occurence, because the check is completed
        for n in range(len(args)):
            if args[n] % i == 0:
                occur += 1
                # Let's check if this happens everytime we check the number on the table
                if occur == len(args):
                    # The number was a divisor of every number of the list, we can add it to the main list
                    commonCoef.append(i)
                    break
                else:
                    continue

    # At the end each common Divisor is on commonCoef, last one is the great common divisor we are looking for
    gcd = commonCoef[len(commonCoef)-1]
    return gcd


main(False)
