"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position, first=0, second=1):
    next = first + second

    if position <= 0:
        return first

    while position >= 0:
        first = second
        second = next
        return get_fib(position - 1, first, second)

def get_fib2(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

# Test cases
print(get_fib2(9))
print(get_fib2(11))
print(get_fib2(0))