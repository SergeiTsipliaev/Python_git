# !!!!!!!!!!!!!!!Тема урока: вложенные циклы!!!!!!!!!!!!!!!

digit = int(input())

for i in range(1, digit + 1):
    for j in range(i + 1):
        if i == j:
            continue
        print(i, end="")
    print()





# num = int(input())

# for i in range(1, (num // 2) + 2):
#     print("*" * i)
# for j in range(num // 2, 0, -1):
#     print("*" * j)

    

# num = int(input())
#
# for i in range(1, num + 1):
#     for j in range(5):
#         print(i, end=" ")
#     print()


# num = int(input())
#
# for i in range(num):
#     for j in range(3):
#         print(num, end=" ")
#     print()


# counter = 0
# for i in range(99, 102):
#     temp = i
#
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)


# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')


# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)


# for i in range(7, -1, -1):
#     for j in range(i + 1):
#         print('*', end='')
#     print()


# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         print(i, j)


# def hourses():
#     for hours in range(24):
#         for minutes in range(60):
#             for seconds in range(60):
#                 print(hours, ':', minutes, ':', seconds)
#     return "Done"
# print(hourses())
