# from collections import namedtuple

# Person = namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# John = Person('John', 'Doe', age=30, birth_place='New York', post_index='10001')
# Oleksii = Person('Oleksii', 'Pavlyk', age=44, birth_place='Kyiv', post_index='02091')

# print(Oleksii.last_name)   # Output: Pavlyk
# print(Oleksii.first_name)  # Output: Oleksii

# print(John.first_name)  # Output: John
# print(John.last_name)   # Output: Doe
# print(John.age)         # Output: 30
# print(John.birth_place) # Output: New York
# print(John.post_index)  # Output: 10001

# import collections

# Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

# cat = Cat('Simon', 4, 'Krabat')

# print(f"This is {cat.nickname}, a {cat.age}-year-old cat owned by {cat.owner}. ")

#Counter

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]

# mark_counts = dict()

# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1

# print(mark_counts)

# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]

# mark_counts = collections.Counter(student_marks)

# print(mark_counts.most_common())

# import collections

# str = 'Banana'

# letter = collections.Counter(str)

# print(letter)

import collections

sentence = "the quick brown fox jumps over the lazy dog"

list_words = sentence.split()
word_count = collections.Counter(list_words)

for word_count.items()