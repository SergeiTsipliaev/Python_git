
string = ["abc", "def", "qsd"]


trigger = False

for i in string:
    for k in i:
        if k == "s":
            print("Find")
            trigger = True
            break
    if trigger:
        break








# while data := input("Введите данные: "):
#     if data == "exit":
#         break
#     print(f"Input: {data}")








# Генерация длины строки, рандом
# from string import  ascii_letters
# from random import  choice
#
# string = ""
#
# for _ in range(int(input("Введите длину строки: "))):
#     string += choice(ascii_letters)
#
#
# print(string)









# lo_limit = 0
# hi_limit = 1000
#
# user_number = int(input(f"Загадайте число от {lo_limit} до {hi_limit}:"))
#
# count = 1
#
# while True:
#     guess_user
