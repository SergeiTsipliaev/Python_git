
# s = input()
#
# for char in s[0::2]:
#     print(char)



# num = int(input())
#
# number = num
# total = ""
#
# while number != 0:
#     procent = number % 2
#     number //= 2
#
#     total += str(procent)
#
# print(total[::-1])

# word = input().lower()
#
# sogl = "бвгджзйклмнпрстфхцчшщ"
# glas = "ауоыиэяюе"
# no_buk = "ёьъ"
#
# count_sogl = 0
# count_glas = 0
#
# for char in range(0, len(word)):
#     if word[char] in sogl:
#         count_sogl += 1
#     elif word[char] in glas:
#         count_glas += 1
#     if word[char] in no_buk:
#         continue
#
# print(f"Количество гласных букв равно {count_glas}")
# print(f"Количество согласных букв равно {count_sogl}")

# n = input()
# total = 0
#
# for num in range(1, len(n)):
#     if n[num] == n[num - 1]:
#         total += 1
#
# print(total)

# n = input()
#
# count1 = 0
# count2 = 0
#
# for c in n:
#     if c == "*":
#         count1 += 1
#     if c == "+":
#         count2 += 1
#
# print("Символ + встречается", count2, "раз")
# print("Символ * встречается", count1, "раз")


# n = input()
#
# flag = True
#
# for c in n:
#     if c.isdigit():
#         flag = False
#
# if flag:
#     print("Цифр нет")
# else:
#     print("Цифра")

# n = input()
# count = 0
# total = sum(int(digit) for digit in n)
# print(total)


# name = input()
# family = input()
# surname = input()
#
# print(name[0], family[0], surname[0], sep="")

# n = input()

# for i in range(-1, -len(n) - 1,  - 1):
#     print(n[i])


# s = input()
#
# for i in range(0, len(s) + 1, 2):
#     print(s[i])


# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')


# s = 'abcdef'
# for c in s:
#     print(c)
