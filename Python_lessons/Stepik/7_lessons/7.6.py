# !!!!!!!!!!!!!!!BREAK, CONTINUE, ELSE!!!!!!!!!!!!!!!

n = 5
while n > 0:
    n -= 1
    print(n)
    if n % 2 == 0:
        break
else:
    print('Цикл завершен.')



# n = int(input())
#
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

# n = int(input())
#
# num = 0
#
# for i in range(2, n+1):
#     if n % i == 0:
#         num = i
#         break
# print(num)


# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20


# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break


# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)
