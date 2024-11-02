# დავალება 1
# list = [53, 35, 32, 5, 8, 6]

# digits = input("Digits [a / r / e]? ").lower()
# if digits == "a":
#    list.append(5)
# elif digits == "r":
#     list.clear()
# else:
#     print("The End")

# print(list)


# დავალება 2
# my_list_1 = [43, '22', 12, 66, 210, ["hi"]]
# index = my_list_1.index(210)
# print(index)

# my_list_1[-1].append("hello")
# print(my_list_1)

# del my_list_1[2]
# print(my_list_1)

# my_list_2 = []
# my_list_2 = my_list_1
# my_list_2.clear()
# print(my_list_1)
# print(my_list_2)
# დავალებ 3
import re

# phone_number = "(123) 456-789"
# pattern = "\(\d{3}\) \d{3}-\d{3}"
# print(re.fullmatch(pattern, phone_number))

phone_number = input("Enter phone number ")
pattern = "\(\d{3}\) \d{3}-\d{3}"

if re.fullmatch(pattern, phone_number):
    print(phone_number)
else:
    print("invalid")    