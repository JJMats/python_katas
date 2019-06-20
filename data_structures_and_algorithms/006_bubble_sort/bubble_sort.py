def bubble_sort(input_array):
    sorted_array = input_array
    elements_to_sort = len(input_array) - 1
    for i in range(len(input_array) - 1):        
        for j in range(elements_to_sort):
            if sorted_array[j] > sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
        
        elements_to_sort -= 1
        #print(sorted_array)

    return sorted_array

print(bubble_sort([21, 2, 5, 6, 7, 1, 18]))
print(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))