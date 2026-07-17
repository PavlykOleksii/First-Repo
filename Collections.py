my_list = list()
empty_list = []

my_list = [1, 2, 3, 4, 5]
print(my_list)  # Виведе: [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)  # Виведе: [1, 2, 3, 4, 5, 6]

my_list = [1, "Oleksii", 3.14, True]
print(my_list)  # Виведе: [1, "Oleksii", 3.14, True]

my_list.append("Pavlyk")
print(my_list)  # Виведе: [1, "Oleksii", 3.14, True, "Pavlyk"]

my_list.reverse()
print(my_list)  # Виведе: ["Pavlyk", True, 3.14, "Oleksii", 1]

my_list.remove(True)
print(my_list)  # Виведе: ["Pavlyk", 3.14, "Oleksii", 1]
print(my_list[2] + " " + my_list[0])  # Виведе: "Oleksii Pavlyk"

my_list [1] = "Pavlovych"
print(my_list[0] + " " + my_list[2] + " " + my_list[1])  
print(my_list.pop(1))  # Виведе: ["Pavlyk", "Pavlovych", "Oleksii", 1]
my_list.append("Pavlovych")
print(my_list)  # Виведе: ["Pavlyk", "Oleksii", 1]

num = [45, 18]
my_list.extend(num)
print(my_list)  # Виведе: ["Pavlyk", "Oleksii", 1, 45, 18]

my_list.insert(2, "Oleksii Pavlovych")
print(my_list)  # Виведе: ["Pavlyk", "Oleksii

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе: "Alice"