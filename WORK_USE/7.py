#вираз, значенням якого є кількість входжень десяткових цифр у рядок s
s = 'abc123def456'
a = sum(1 for char in s if char.isdigit())
print(a)
