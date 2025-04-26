













#!!!!!!!!!!!!!!!!!ZIP!!!!!!!!!!!!!!!!!
# my_list = []
#
# for i in range(20):
#     if i % 2:
#         my_list.append(i ** 2)
#
# print(my_list)

#------листкомперхеншен(можно сет, дикт, тюпл)
# letters = list("1234567890")
#
# my_list = {i: int(i) for i in letters if i.isdigit()} #-> так словарь пишем
#
# # my_list = {int(i) for i in letters if i.isdigit()}
#
# print(my_list )





# from itertools import zip_longest
#
# numbers = (1, 2, 3, 4, 5)
# letters = "a", "b", "c"
# p = list("fjhyqaegsgsde")
#
# # result = []
# # for i in range(len(numbers)):
# #     result.append((numbers[i], letters[i]))
#
# result = list(zip_longest(numbers, letters, p, fillvalue="NO"))
#
# print(result)

# !!!!!!!!!!!!!!!!!LAMBDA!!!!!!!!!!!!!!!!!

# def custom_sum(x, y):
#     return x + y
#
#
# # lambda x,y: x + y
#
#
# numbers = list("12345678")
# print(numbers)
#
# numbers = list(map(int, filter(lambda x: int(x) % 2, numbers)))
# print(numbers)

# !!!!!!!!!!!!!!!!!ARGS, KWARGS!!!!!!!!!!!!!!!!!

#
# def custom_sum(*args):
#     result = 0
#     for item in args:
#         result += item
#     return result
#
#
# print(custom_sum(23, 44))

# !!!!!!!!!!!!!!!!!АРГУМЕНТЫ, Return!!!!!!!!!!!!!!!!!

# def int_input(message="Please input text: ", msg_error="Is it not number"):
#     while True:
#         data = input(f"Input text {message}")
#         if data.isdigit():
#             return int(data), 3, 4, 5
#         print(msg_error)
#
#
# a, b, *c = int_input()
# print(a)
# print(b)
# print(c)

# !!!!!!!!!!!!!!!!!ПОНЯТИЕ ФУНКЦИИ!!!!!!!!!!!!!!!!!

# def greetings(name="Kate", age=18, work=None):
#     print(f"Hello, {name}! You {age}? Your work {work}")
#
#     if age > 20:
#         return "Old man"
#     return "Small"
#
#
# print('AFTER\n')
# # greetings("Vadim", age=40)
# # greetings("Ivan", work="Management")
# # greetings("Nadeshda", work="IT")  # вызов функции
# result = greetings(age=18)
# print(result)
# print("BEFORE")
