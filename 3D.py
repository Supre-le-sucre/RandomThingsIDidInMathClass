def main(debug=False):
    A = [0, 0, 0]
    B = [0, 0, 0]
    C = [0, 0, 0]
    while True:
        user = input(">>> ")
        if debug: print(user)

        # ---------------------
        if user == "h":
            # Help command
            print("=-= Help =-= \na defines A etc. \npt returns defined points \npl returns a plan")
        # ---------------------
        # ---------------------
        elif user == "a" or user == "b" or user == "c":
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

        # ---------------------
        # ---------------------
        elif user == "pt":
            # Return points coordinates
            coordinatesFormat("A", A)
            coordinatesFormat("B", B)
            coordinatesFormat("C", C)
        # ---------------------
        # ---------------------
        elif user == "pl":
            # Return system and cartesian equation of plan
            u = vectorCalc(A, B)
            v = vectorCalc(A, C)
            thereIsAPlan = True
            k1 = u[0] - v[0]
            k2 = u[1] - v[1]
            k3 = u[2] - v[2]
            if k1 == k2 == k3:
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

                d = 0
                for i in range(3):
                    if vectorN[i] != 0:
                        # This calculates the d at the end of the cartesian equation
                        d -= vectorN[i] + A[i]
                        if i == 0:
                            cartesianEquation += str(vectorN[i]) + "x"
                        if i == 1:
                            if not cartesianEquation == "":
                                if vectorN[i] > 0:
                                    cartesianEquation += " + " + str(vectorN[i]) + "y"
                                else:
                                    cartesianEquation += " - " + str(abs(vectorN[i])) + "y"
                            else:
                                cartesianEquation += str(vectorN[i]) + "y"
                        if i == 2:
                            if not cartesianEquation == "":
                                if vectorN[i] > 0:
                                    cartesianEquation += " + " + str(vectorN[i]) + "z"
                                else:
                                    cartesianEquation += " - " + str(abs(vectorN[i])) + "z"
                            else:
                                cartesianEquation += str(vectorN[i]) + "z"

                if d > 0:
                    cartesianEquation += " + " + str(d)
                elif d < 0:
                    cartesianEquation += " - " + str(abs(d))

                cartesianEquation += " = 0"
                print(cartesianEquation)

            else:
                # There is no equation of plan to display because vectors are collinear
                print("Nothing to see here :/")


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


main()
