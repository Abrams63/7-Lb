data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#З першої половини послідовності (якщо довжина непарна, центральний елемент включити)
def first_half_inclusive(data):
    length = 0
    for _ in data:
        length += 1
    middle = (length + 1) // 2
    for i, item in enumerate(data):
        if i < middle:
            yield item


first_half_inclusive(data)

#З першої половини послідовності (якщо довжина непарна, центральний елемент не включати)
def first_half_exclusive(data):
    length = 0
    for _ in data:
        length += 1
    middle = length // 2
    for i, item in enumerate(data):
        if i < middle:
            yield item

first_half_exclusive(data)

#З першої третини послідовності:
def first_third(data):
    length = 0
    for _ in data:
        length += 1
    third = length // 3
    for i, item in enumerate(data):
        if i < third:
            yield item

first_third(data)

#З другої половини послідовності (якщо довжина непарна, центральний елемент включити)
def second_half_inclusive(data):
    length = 0
    for _ in data:
        length += 1
    middle = length // 2
    for i, item in enumerate(data):
        if i >= middle:
            yield item

second_half_inclusive(data)

#З другої третини послідовності:
def second_third(data):
    length = 0
    for _ in data:
        length += 1
    start = length // 3
    end = 2 * length // 3
    for i, item in enumerate(data):
        if start <= i < end:
            yield item

second_third(data)

#З кожного третього елемента послідовності:
def every_third(data):
    for i, item in enumerate(data):
        if (i + 1) % 3 == 0:
            yield item

every_third(data)

#З кожного третього елемента послідовності, записаних в оберненому порядку:
def every_third_reversed(data):
    third_elements = []
    for i, item in enumerate(data):
        if (i + 1) % 3 == 0:
            third_elements.append(item)
    for item in reversed(third_elements):
        yield item

every_third_reversed(data)