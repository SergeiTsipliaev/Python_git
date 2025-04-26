# !!!!!!!!!!!!!!!Тема урока: ревью кода!!!!!!!!!!!!!!!







# n = int(input())
# multiply = 1
# while n != 0:
#     digit = n % 10
#     multiply *= digit
#     n //= 10
# print(multiply)


# n = int(input())
# one_digit = 0
# while n > 0:
#     last_digit = n % 10
#     one_digit = last_digit
#     n //= 10
# print(one_digit)


# n = int(input())
# max_digit = -1
# while n != 0:
#     digit = n % 10
#     if digit % 3 == 0 and digit > max_digit:
#         max_digit = digit
#     n //= 10
# if max_digit < 0:
#     print('NO')
# else:
#     print(max_digit)


# s = 0
# for i in range(1, 8):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# if s % 2 == 0 and s != 0:
#     print(s)
# else:
#     print("0")


# mx = -10 ** 6
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if mx < x < 0:
#         mx = x
#
# if s >= 0:
#     print("NO")
# else:
#     print(s)
#     print(mx)

# count = 0
# multiply = 1
# for _ in range(10):
#     digit = int(input())
#     if digit > 0:
#         count += 1
#         multiply *= digit
#
# if count > 0:
#     print(count, multiply, sep="\n")
# else:
#     print('NO')
