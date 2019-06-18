"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    input_array.sort()
    
    min_idx = 0
    max_idx = len(input_array) - 1

    while(min_idx <= max_idx):
        mid_idx = int((min_idx + max_idx) / 2)
        if input_array[mid_idx] == value:
            return mid_idx
        elif input_array[mid_idx] < value:
            min_idx = mid_idx + 1
        else:
            max_idx = mid_idx - 1

    return -1

test_list = [1,3,9,11,15,19,25,29]
test_val1 = 25
test_val2 = 15
test_val3 = 2
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, test_val3))