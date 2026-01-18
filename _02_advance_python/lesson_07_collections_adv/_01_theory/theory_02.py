from collections import deque

# добавление элементов
d = deque()
d.append(10)
d.appendleft(5)
print(d)
print()

# удаление элементов
nums_d = deque([1, 2, 3])
last_item = nums_d.pop()
print(last_item)
first_item = nums_d.popleft()
print(first_item)
print(nums_d)
print()

# удаление элементов
d2 = deque([1, 2, 3, 4])
print(d2[0], d2[1], d2[-1])
print()

# ограничение длины очереди
d3 = deque(maxlen=3)
d3.append(1)
d3.append(2)
d3.append(3)
print(d3)
d3.append(4)
print(d3)
d3.appendleft(5)
print(d3)
print()

# перестановка (ротация) элементов
d4 = deque([1, 2, 3, 4])
d4.rotate(1)  # >> 1 шаг
print(d4)
d4.rotate(-2)  # << 2 шага
print(d4)

# расширение очереди
d5 = deque([3, 4])
d5.extend([5, 6])
print(d5)
d5.extendleft([2, 1])
print(d5)
d5.reverse()
print(d5)
