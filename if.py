# # # # num = 15
# # # # if num > 10:
# # # #     print(f"Число {num} більше за 10")
# # # # else: 
# # # #     print(f"Число {num} менше або дорівнює 10")

# # # # x = int(input("Введіть число: "))
# # # # if x % 2 == 0:
# # # #     print(f"Число {x} є парним")
# # # # else:
# # # #     print(f"Число {x} є непарним")

# # # # a = int(input("Введіть перше число: "))
# # # # if a > 0:
# # # #     print(f"Число {a} є додатнім")
# # # # elif a < 0:
# # # #     print(f"Число {a} є від'ємним")
# # # # else:
# # # #     print(f"Число {a} дорівнює 0")

# # # money = 0
# # # if money:
# # #     print(f"You have {money} on your bank account")
# # # else:
# # #     print("You have no money and no debts")

# # # result = None
# # # if result:
# # #     print(result)
# # # else:
# # #     print("Result is None, do something")

# # # # user_name = input("Enter your name: ")

# # # # if user_name:
# # # #     print(f"Hello {user_name}")
# # # # else:
# # # #     print("Hi Anonym!")

# # # a = [1, 2, 3]
# # # b = a
# # # c = [1, 2, 3]

# # # print(a is b)  # Виведе: True, оскільки b посилається на той самий об'єкт, що і a
# # # print(a is c)  # Виведе: False, оскільки c є новим об'єктом, хоча його значення збігаються з a

# # num = int(input("Введіть число: "))
# # length = len(str(num))

# # if length == 2 and num % 2 == 0:
# #     print(f"Число {num} є двозначним і парним")
# # else:
# #     print(f"Число {num} не є двозначним або не є парним")

# num = int(input("Введіть число: "))

# if num % 3 == 0 and num % 5 == 0:
#     print(f"FizzBuzz: Число {num} ділиться на 3 і на 5")
# elif num % 3 == 0:
#     print(f"Fizz: Число {num} ділиться на 3")
# elif num % 5 == 0:
#     print(f"Buzz: Число {num} ділиться на 5")
# else:
#     print(f"Число {num} не ділиться на 3 або на 5")

# x = int(input("Введіть число X: "))
# y = int(input("Введіть ще одне число Y : "))

# if x == 0:
#     print(f"Число X дорівнює 0")
#     x = int(input("Введіть нове число X: "))

#     result = y/x
#     print(f"Результат ділення Y на X: {result}")

x = int(input("Введіть число X: "))
y = int(input("Введіть ще одне число Y : "))

if x >= 0:
    if y >= 0:
        print(f"Перша чверть.")
    else:
        print(f"Четверта чверть.")
else:
    if y >= 0:
        print(f"Друга чверть.")
    else:
        print(f"Третя чверть.")
