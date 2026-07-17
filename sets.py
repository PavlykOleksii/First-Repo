empty_set = set()

a = set("Pavlyk Oleksii Pavlovych")
print(a)  # Виведе: {' ', 'P', 'a', 'v', 'l', 'y', 'k', 'O', 'e', 's', 'i', 'P', 'a', 'v', 'l', 'o', 'v', 'y', 'c', 'h'}
a.update("Slava Ukraini")
print(a)  # Виведе: {' ', 'P', 'a', 'v', 'l', 'y', 'k', 'O', 'e', 's', 'i', 'S', 'U', 'n', 't', 'r', 'c', 'h'}

a.clear()

a = {1,2,3}
b = {3,4,5}

print(a.intersection(b))   # Виведе: {3}
print(b.intersection(a))          # Виведе: {3}
print(a & b)          # Виведе: {3}
print(a.union(b))          # Виведе: {1, 2, 3, 4, 5}
print(b.union(a))          # Виведе: {1, 2, 3, 4, 5}

print(a.difference(b))          # Виведе: {1, 2}
print(b.difference(a))          # Виведе: {4, 5}
print(a - b)          # Виведе: {1, 2}
print(b - a)          # Виведе: {4, 5}

print(a.symmetric_difference(b))          # Виведе: {1, 2, 4, 5}
print(b.symmetric_difference(a))          # Виведе: {1, 2, 4, 5}