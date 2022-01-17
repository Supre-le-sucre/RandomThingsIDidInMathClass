def main(debug=False):
    A = [0, 0, 0]
    B = [0, 0, 0]
    C = [0, 0, 0]
    while True:
        user = input(">>> ")
        if debug : print(user)

        # ---------------------
        if user == "h":
            # Help command
            print("=-= Help =-= \na defines A etc. \npt returns defined points \npl returns a plan")
        # ---------------------
        # ---------------------
        elif user == "a" or user == "b" or user == "c" :
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
            system = " | x = "
            for n in range(3):
                # Construction of system
                if n == 1:
                    system += "<| y = "
                elif n == 2:
                    system += " | z = "
                system += str(A[n])
                if u[n] > 0:
                    system += " + " + str(u[n]) + "k"
                elif u[n] < 0:
                    system += " - " + str(abs(u[n])) + "k"
                if v[n] > 0:
                    system += " + " + str(v[n]) + "k'"
                elif v[n] < 0:
                    system += " - " + str(abs(v[n])) + "k'"
                system += "\n"
            print(system)


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
    return [(y*zp - yp*z) , (z*xp - zp*x), (x*yp-y*xp)]


def isNumeral(str):
    # Check if a str is a number
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if '-' in str and len(str) > 1:
        # If str contains - remove minus before testing. We could have added the minus in the number table,
        # but this could cause the symbol minus to be considered a number and therefore returns an errors when cast
        # as an integer
        str = str[1:len(str)]
    for n in range (len(str)):
        if not str[n] in numbers:
            return False
    return True


main(True)
