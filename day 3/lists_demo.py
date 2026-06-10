# list demo
mixed_list = [23, "Prithvi", 56.79, True, None]
# print(mixed_list)
empty_list = []

from_range = list(range(1,11))
from_str = list("Python")

# print(from_range)
# print(from_str)

# print(from_range[0])
# print(from_range[-1])
# print(from_range[2:6])

# print(8 in from_range)
# print(2 not in from_range)

#list methods
# from_range.append(23)
# print('Append: ', from_range)

# from_range.insert(3, 14)
# print('Insert: ', from_range)

# # remove from list
# ele = from_range.pop()  #=>removes the last item
# # print(f'Popped element: {ele:12}, List: {from_range}')
# print('Popped Element: ', ele, ', List: ', from_range)

# popped_ele = from_range.pop(3)
# print(f'Popped element: {popped_ele}, List: {from_range}')

# from_range.remove(4)
# print('Remove: ', from_range)

# Sorting, Searching and Counting
# grades = [45, 80, 60, "Alpha", 34, "Mark", True]
grades = [45, 80, 60, 34, 56]
print('Before Sorting: ', grades)

# sort in place
# grades.sort()
# print('After Sorting (asc): ', grades)

# grades.sort(reverse=True)  # sorting in desc order
# print('After Sorting (desc): ', grades)

# new_list = sorted(grades)
# print('New List: ', new_list)

# fruits = ['banana', 'MANGO', 'apple', 'Grapes', 'pineApple', 'figs']

fruits = ['banana', 'MANGO', 'apple', 'Grapes', 'pineApple', 'figs', ['almonds', 'pista', 'cashew']]

# sorted_fruits = sorted(fruits, key=len)

# sorted_fruits = sorted(fruits, key=lambda n:n.lower())
# print(sorted_fruits)

#method 1 - flatten the nested list
# flat_list = []
# for fruit in fruits:
#     if isinstance(fruit, list):
#         flat_list.extend(fruit)
#     else:
#         flat_list.append(fruit)
    
# sorted_list = sorted(flat_list)
# print(sorted_list)

# method 2 - sort inner list in place
# for fruit in fruits:
#     if isinstance(fruit, list):
#         fruit.sort()
    
# print(fruits)

# # method 3: sort outer list, also sort the inner list
# result = sorted(
#     [sorted(x) if isinstance(x, list) else x for x in fruits],
#     key=lambda x: x[0] if isinstance(x, list) else x
# )

# print(result)

# for x in fruits:
#     if isinstance(x, list):
#         result.extend(sorted(x))
#     else:
#         result.append(x)

# searching
position = fruits.index('MANGO')
print(position)

# 11/06 => list comprehensions, tuples, dicts, sets



