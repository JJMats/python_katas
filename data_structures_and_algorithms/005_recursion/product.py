def product(x, y):
    if y == 0:
        return 0
    p = product(x, y-1)
    return p+x

def product2(x, y):
    if y == 1:
        return x

    return x + product2(x, y - 1)
