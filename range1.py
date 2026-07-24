# for i in range(5):
#     print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# some_list = ["apple", "banana", "cherry"]
# for index, value in enumerate(some_list):
#     print(index, value)

# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for number, letter in zip(list1, list2):
#     print(number, letter)

# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }

# for key in numbers:
#     print(key)

# for key in numbers.keys():
#     print(key)

# for val in numbers.values():
#     print(val)

# for key, value in numbers.items():
#     print(key, value)

# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")

age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")
