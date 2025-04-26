s = input()

count = 0

for i in range(len(s)):
    if s[i].isdigit():
        continue
    elif s[i].islower():
        count += 1
print(count)

# s = input()
# s = s.lower()
#
# if "хорош" in s:
#     print("YES")
# else:
#     print("NO")


# s = input()
#
# print(s.swapcase())


# s = input()
#
# if s.title() == s:
#     print("YES")
# else:
#     print("NO")
