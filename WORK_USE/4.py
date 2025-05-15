
numbers = [1, 2.5, 'hello', 3, 4.0, 'world', 5]

#Підпослідовність елементів, що є цілими числами (int):
f = (x for x in numbers if isinstance(x, int))

#Підпослідовність елементів, що є числами з плаваючою комою (float):
g = (x for x in numbers if isinstance(x, float))

#Підпослідовність елементів, що не є числами з плаваючою комою (float):
h = (x for x in numbers if not isinstance(x, float))

#Підпослідовність елементів, що є рядками (str):
i = (x for x in numbers if isinstance(x, str))



