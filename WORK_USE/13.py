# вирази, які перевіряють, чи всі елементи числової послідовності data є додатними або цілими відповідно:
data = [1, 2, 3, 4, 5, 6]
#Чи всі елементи є додатними:
a =  all(element > 0 for element in data if isinstance(element, (int, float)))
print(a)
#Чи всі елементи є цілими:
b = all(isinstance(element, int) for element in data)
print(b)