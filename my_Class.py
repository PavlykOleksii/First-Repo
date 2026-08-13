# class User:
#     name = 'Anonymous'
#     age = 15

# user1 = User()
# print(user1.name)
# print(user1.age)

# user2 = User()
# user2.name = "John"
# user2.age = 90

# print(user2.name)
# print(user2.age)

# class MyClass:
#     def __init__(self, value):
#         self.instance_field = value  # Поле класу

# obj1 = MyClass(5)
# obj2 = MyClass(10)

# print(obj1.instance_field)  # Виведе: 5
# print(obj2.instance_field)  # Виведе: 10

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def say_name(self):
#         print(f"My name is {self.name}. I am {self.age} years old.")

#     def set_age(self, new_age: int):
#         self.age = new_age

# bob = Person("Oleksii", 44)

# bob.say_name()  # Виведе: My name is Oleksii. I am 44 years old.
# bob.set_age(40)
# bob.say_name()  # Виведе: My name is Oleksii. I am 40 years old.

# class Person:
#     count = 0  # Класове поле

#     def __init__(self, name: str):
#         self.name = name
#         Person.count +=1

#     def how_many_person(self):
#         print(f"К-ть людей зараз {Person.count}")

# first = Person("Oleksii")
# first.how_many_person()

# sec = Person("July")
# sec.how_many_person()

