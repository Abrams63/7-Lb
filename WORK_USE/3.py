import math

# Example list of numbers; replace with your actual data as needed
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Підпослідовність елементів, що діляться на 2:
a = (x for x in numbers if x % 2 == 0)

#Підпослідовність елементів, що не діляться на жодне з чисел 2, 3, 5:
b = (x for x in numbers if x % 2 != 0 and x % 3 != 0 and x % 5 != 0)

#Підпослідовність елементів, більших за задане число n:
c = (x for x in numbers if x > n)

#Підпослідовність додатних елементів:
d = (x for x in numbers if x > 0)

#Підпослідовність простих чисел:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

(x for x in numbers if is_prime(x))

#Підпослідовність точних квадратів:
e =(x for x in numbers if math.sqrt(x) == int(math.sqrt(x)) and x >= 0)