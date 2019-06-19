def getFib(position):
    if position == 0:
        return 0

    if position == 1:
        return 1

    first = 0
    second = 1
    next = first + second
    i = 2
    while i < position:
        first = second
        second = next
        next = first + second
        i += 1

    return next

print(getFib(0))
print(getFib(1))
print(getFib(8))