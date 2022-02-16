def prime(n):
    tab = [2]
    # Show all prime numbers until n
    for number in range(2, n+1):
        for i in range(len(tab)):
            if number % tab[i] == 0:
                break
        if i == len(tab)-1 and number != 2:
            tab.append(number)
    return tab
