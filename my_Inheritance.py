# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self) -> str:
#         return "Мяу"

# class Dog(Animal):
#     def __init__(self, nickname: str, age: int, breed: str):
#         super().__init__(nickname, age)
#         self.breed = breed

#     def make_sound(self):
#         return "Гав"

# class Cow(Animal):
#     def make_sound(self):
#         return "Мууууу"

# my_cat = Cat("Буся", 8)
# my_dog = Dog("Барсік", 12, "Пітбуль")
# my_cow = Cow("мУРКАК", 15)

# print(my_cat.make_sound())
# print(my_dog.make_sound())
# print(my_cow.make_sound())
# print(my_dog.breed)

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # Виведе порядок розв'язання методів для класу D
