def binomial(k, n, p):
    # f is the combinatorial we need in order to get the correct value
    # if we are dealing with a null we need this in order to avoid dividing by 0
    if k == 0:
        f = 1
    else:
        f = n / k
    for i in range(1, k):
        # To be less consuming, the combinatorial has been simplified to avoid factorials calculus
        f *= (n - i) / (k - i)
    return f * (p ** k) * ((1 - p) ** (n - k))


def proba(k):
    p = 0
    for i in range(0, k + 1):
        p += binomial(i, 20, 0.25)
    return p
