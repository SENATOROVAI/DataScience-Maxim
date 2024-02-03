# Пример 1
numbers_list = [1, 1, 2, 2, 3, 3, 4, 4]

numbers_list_ordered = sorted(numbers_list, reverse=True)
numbers_set = set(numbers_list)
numbers_set.add(max(numbers_list) + 1)

b = set(numbers_list) - {min(numbers_list), }
numbers_frozenset = frozenset(b)
print(numbers_set)

