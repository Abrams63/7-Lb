#Звичайно, ось вирази, які перевіряють, чи всі елементи послідовності цілих чисел data відповідають заданим критеріям:
data = [7, 14, 21, 28, 35]
#Чи всі елементи діляться на 7:
a = all(number % 7 == 0 for number in data)
print(a)
#Чи всі елементи більші за задане число n:
n = 5
b = all(number > n for number in data)
print(b)
#Чи всі елементи є точними квадратами:
c = all((number**0.5).is_integer() for number in data)
print(c)
#Чи всі елементи є простими числами:
import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

all(is_prime(element) for element in data)