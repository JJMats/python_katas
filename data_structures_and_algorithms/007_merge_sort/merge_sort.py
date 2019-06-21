'''
Merge Sort Problem

Divide and conquer by continually splitting a list in half via
recursion. Once the halves are sorted, they are then merged 
back together in sorted order.

Time Complexity: O(n log n)
Auxiliary Space: O(n)
'''
def merge_sort(array, left_idx, right_idx):
    if len(array) > 1:
        mid_idx = len(array) // 2
        left_half = array[left_idx:mid_idx]
        right_half = array[mid_idx:right_idx]

        # Recursively call merge_sort to break arrays down to single
        #  elements
        merge_sort(left_half, 0, len(left_half))
        merge_sort(right_half, 0, len(right_half))

        i = j = k = 0

        # Check the head of each array half and pull the lowest value
        # Add the lowest value back to the original array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # Add any remaining elements in arrays (which are now sorted)
        #  back to the original array
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array

array_to_sort = [12, 51, 11, 22, 24, 1, 7, 99, 101]
sorted_array = merge_sort(array_to_sort, 0, len(array_to_sort))
print(sorted_array)