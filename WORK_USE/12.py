#вираз, значенням якого для послідовності цілих чисел data є сума її елементів, що займають парні позиції (індекси):
data = [1, 2, 3, 4, 5, 6]
a = sum(element for index, element in enumerate(data) if index % 2 == 0)
print(a)
b = sum(element for index, element in enumerate(data) if index % 2 != 0)
print(b)