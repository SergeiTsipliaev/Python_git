



# s = input()
#
# h1 = s.find("h")
# h2 = s.rfind("h")
#
# print(s[:h1], s[h2 + 1:], sep="")



# s = input()
#
# if s.count("f") == 1:
#     print(s.find("f"))
# elif s.count("f") > 1:
#     print(s.find("f"), s.rfind("f"))
# elif s.count("f") == 0:
#     print("NO")


# s = input()
# s = s.strip()
#
# count = 0
#
# count2 = 0
#
# for i in s:
#     if s.count(i) >= count:
#         count = s.count(i)
#         count2 = i
#
# print(count2)

# s = input()
#
# if s.endswith(".com") or s.endswith(".ru"):
#     print("YES")
# else:
#     print("NO")


# s = input()
#
# count = 0
#
# for i in range(len(s)):
#     if s[i].isdigit():
#         count += 1
#
# print(count)

# n = int(input())
#
# count = 0
#
# for i in range(n):
#     word = input()
#     if word.count("11") >= 3:
#         count += 1
# print(count)


# s = input()
# s = s.lower()
#
# a = s.count("а")
# g = s.count("г")
# c = s.count("ц")
# t = s.count("т")
#
# print(f"Аденин: {a}")
# print(f"Гуанин: {g}")
# print(f"Цитозин: {c}")
# print(f"Тимин: {t}")

# s = input()
#
# if s.count(" ") > 0:
#     print(s.count(" ") + 1)
# elif s.count(" ") == 0:
#     print("1")
