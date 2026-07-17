my_dict = {"name": "Alice", "age": 25, "city": "New York"}

print(my_dict)  # Виведе: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict["city"])  # Виведе: "New York"

my_dict["age"] = 44
my_dict["name"] = "Oleksii"
my_dict["email"] = "pavlyk.oleksii@gmail.com"
print(my_dict["email"])  # Виведе: "pavlyk.oleksii@gmail.com"
del my_dict["city"]

my_dict["city"] = "Sambir"
print(my_dict["city"])  # Виведе: "Sambir"

if "name" in my_dict:
    print("Name is in the dictionary:", my_dict["name"])  # Виведе: "Name is in the dictionary: Oleksii"
if "age" in my_dict:
    print("Age is in the dictionary:", my_dict["age"])  # Виведе: "Age is in the dictionary: 44"
if "second_name" in my_dict:
    print("Second name is in the dictionary:", my_dict["second_name"])  # Виведе: "Second name is in the dictionary: Petrov"
else:
    print("Second name is not in the dictionary.")  # Виведе: "Second name is not in the dictionary."
    my_dict["second_name"] = input("Введи прізвище: ")  # Введи прізвище: Petrov
    print("Second name is now in the dictionary:", my_dict["second_name"])  # Виведе: "Second name is now in the dictionary: Petrov"

    my_dict.update({"wife": "July", "wage": 40})
    print(my_dict)  # Виведе: {'name': 'Oleksii', 'age': 44, 'email': 'pavlyk.oleksii@gmail.com', 'city': 'Sambir', 'second_name': 'Petrov', 'wife': 'July', 'wage': 40}

    cmy_dict = my_dict.copy()
    cmy_dict.clear()
    print(cmy_dict)  # Виведе: {'name': 'Oleksii