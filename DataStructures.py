# def create_stack():
#     return[]

# def is_empty(stack):
#     return len(stack) == 0

# def push(stack, item):
#     stack.append(item)

# def pop(stack):
#     if not is_empty(stack):
#         return stack.pop()
#     else:
#         print("Стек пустий")

# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else:
#         print("Стек пустий")

# stack = create_stack()

# push(stack,"a")
# push(stack,"B")
# push(stack,"X")

# #print(stack)

# print(peek(stack))

# from collections import deque

# queue = deque()

# queue.append("O")
# queue.append("L")
# queue.append("E")

# print("Черга після додавання елементів:", list(queue))
# print("Видалений елемент:", queue.popleft())
# print("Черга після додавання елементів:", list(queue))

# from collections import deque

# # Створення пустої двосторонньої черги
# d = deque()

# # Додаємо елементи в чергу
# d.append('middle')  # Додаємо 'middle' у кінець черги
# d.append('last')    # Додаємо 'last' у кінець черги
# d.appendleft('first')  # Додаємо 'first' на початок черги

# # Виведення поточного стану черги
# print("Черга після додавання елементів:", list(d))

# # Видалення та виведення останнього елемента (з правого кінця)
# print("Видалений останній елемент:", d.pop())

# # Видалення та виведення першого елемента (з лівого кінця)
# print("Видалений перший елемент:", d.popleft())

# # Виведення поточного стану черги після видалення елементів
# print("Черга після видалення елементів:", list(d))

# from collections import deque

# q = deque(maxlen=5)

# for i in range(10):
#     q.append(i)

# print(q)

from collections import deque

tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]

task_queue = deque()

for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)
        print(f"Додано швидке завдвння: {task["name"]}")
    else:
        task_queue.append(task)
        print(f"Додано повільне завдання: {task['name']}")

#print(task_queue)

while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")