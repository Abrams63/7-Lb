#вираз, значенням якого є найменший додатний елемент послідовності data або None, якщо таких елементів у послідовності немає:
data = [1, -2, 3, 4, -5, 6, 7, 8, 9, 10]
a = min((element for element in data if isinstance(element, (int, float)) and element > 0), default=None)
print(a)