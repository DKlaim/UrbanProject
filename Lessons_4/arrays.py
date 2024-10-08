from SortFunc.sort_func import insertion_sort, bubble_sort, selection_sort

data_1 = [9, 5, 6, 4, 8, 7, 3, 2, 1]
data_2 = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'b', 'v', 'c', 'x', 'z']
data_3 = ['9', '5', '6', '4', '8', '7', '3', '2', '1', 'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'b', 'v', 'c', 'x', 'z']


print(insertion_sort(data_1))
print(insertion_sort(data_2))
print(insertion_sort(data_3))
print()

print(bubble_sort(data_1))
print(bubble_sort(data_2))
print(bubble_sort(data_3))
print()

print(selection_sort(data_1))
print(selection_sort(data_2))
print(selection_sort(data_3))