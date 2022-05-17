from random import randint


def bruteForce(n=1):
    L = []
    for i in range(n):
        L.append(i)

    choose = -1
    times = 0
    numberToGet = randint(0, n)
    while choose != numberToGet:
        if len(L) - 1 == 0:
            return n
        index = randint(0, len(L) - 1)
        choose = L[index]
        times += 1
        if choose != numberToGet:
            L.remove(choose)
            continue
    return times


def multipleBruteForce(times=1, n=1):
    sum = 0
    for k in range(times):
        if randint(0, 9999) == 0:
            print("Loading... " + str(progression(k, times)) + "%")
        sum += bruteForce(n)
    return sum / times


def progression(actual, max):
    return actual * 100 / max


print(multipleBruteForce(1))
