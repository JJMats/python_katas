def sum_cube(x):
    if x == 1:
        return 1

    s = sum_cube(x - 1)

    return x**3 + s


def sum_cube2(x):
    if x == 1:
        return 1

    return x**3 + sum_cube2(x-1)
