def prime(n):
    tab = [2]
    # Show all prime numbers until n
    for number in range(3, n + 1):
        for i in range(len(tab)):
            if number % tab[i] == 0:
                break
        if i == len(tab) - 1:
            tab.append(number)
    return tab
