
s = input()
result = ""
i = 0
while i < len(s):
    if s[i:i+3] == "[u-":
        j = i + 3
        num_str = ""
        while j < len(s) and s[j] != "]":
            num_str += s[j]
            j += 1
        if j < len(s) and s[j] == "]":
            num = int(num_str)
            result += chr(num)
            i = j + 1
        else:
            result += s[i]
            i += 1
    else:
        result += s[i]
        i += 1
print(result)


# n = int(input())
# s = input()
#
# decoded = ''
# for c in s:
#     decoded += chr((ord(c) - ord('a') - n) % 26 + ord('a'))
#
# print(decoded)



# s = input()
#
# count = 0
# new_count = 0
# english = "eyopaxcETOPAHXCBM"
# russian = "еуорахсЕТОРАНХСВМ"
#
#
# for i in range(len(s)):
#     count += ord(s[i])
#
# for i in range(len(english)):
#     s =  s.replace(english[i], russian[i])
#
# for i in range(len(s)):
#     new_count += ord(s[i])
#
# print(f"Старая стоимость: {count * 3}🐝\nНовая стоимость: {new_count * 3}🐝")



# s = input()
#
# count = 0
#
# for i in range(len(s)):
#     count += ord(s[i])
#
# print(f"Текст сообщения: '{s}'\nСтоимость сообщения: {count * 3}🐝")

# s1 = input()
# s2 = input()
# s3 = input()
# s4 = input()
#
# a = 0
# b = 0
# c = 0
# d = 0
#
# for i in range(len(s1)):
#     a += ord(s1[i])
# for i in range(len(s2)):
#     b += ord(s2[i])
# for i in range(len(s3)):
#     c += ord(s3[i])
# for i in range(len(s4)):
#     d += ord(s4[i])
#
# if max(a, b, c, d) == a:
#     print(s1)
# elif max(a, b, c, d) == b:
#     print(s2)
# elif max(a, b, c, d) == c:
#     print(s3)
# elif max(a, b, c, d) == d:
#     print(s4)

# s = input()
#
# for i in range(len(s)):
#     print(ord(s[i]), end=" ")

# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     print(chr(i), end=" ")

# s = input()
#
#
# if ord(s) >= 1071:
#     print("Дальше букв нет")
# else:
#     for _ in range(1):
#         print(chr(ord(s) + 1))
