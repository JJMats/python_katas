'''
Quick Sort Problem

Divide and conquer, but do not use additional storage.

First, select a pivot value (here we are using the first
list item).

Next, partition the data - move items that are on the wrong
side of the pivot value while converging on the split point.

Recursively call the partitioning function to sort the data.

Time Complexity: O(n log n), worst case - O(n^2)
Auxiliary Space: O(n)
'''

def quick_sort(input):
    quick_sort_helper(input, 0, len(input) - 1)

def quick_sort_helper(input, first, last):
    if first < last:
        split_point = partition(input, first, last)
        # Recursively sort the partitioned data
        quick_sort_helper(input, first, split_point - 1)
        quick_sort_helper(input, split_point + 1, last)

def partition(input, first, last):
    pivot_val = input[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and input[left_mark] <= pivot_val:
            left_mark += 1

        while input[right_mark] >= pivot_val and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            input[left_mark], input[right_mark] = input[right_mark], input[left_mark]

    input[first], input[right_mark] = input[right_mark], input[first]

    return right_mark

input = [12, 84, 1, 22, 14, 13, 16, 63, 2]
quick_sort(input)
print(input)