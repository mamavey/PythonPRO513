from collections import Counter

text = "Hello World"
print(Counter(text))

words = ['python', 'java', 'python', 'C++', 'java', 'python']
counter = Counter(words)
print(counter.most_common(2))

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(Counter(numbers))
