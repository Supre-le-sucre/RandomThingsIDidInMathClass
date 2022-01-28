def conway(n):
    term = "1"
    for i in range(n - 1):
        print("Loading... "+str(i)+" / "+str(n))
        nextTerm = ""
        count = 0
        check = term[0]
        for index in range(len(term)):
            if term[index] != check:
                nextTerm += str(count) + str(check)
                check = term[index]
                count = 0
            if term[index] == check:
                count += 1
            if index == (len(term) - 1):
                nextTerm += str(count) + str(check)
        term = nextTerm
    return term
