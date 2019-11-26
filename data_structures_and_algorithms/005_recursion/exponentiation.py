def exponentiation(r, n):
    if n == 0:
        return r
    
    p = exponentiation(r, n-1)
    return p**2


def exponentiation2(r, n):
    if n == 0:
        return r

    return exponentiation2(r, n-1)**2
