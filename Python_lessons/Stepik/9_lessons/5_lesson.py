# s = input()
#
# if s.startswith("@") and 5 <= len(s) <= 15 :
#     valid = True
#     for i in s[1:]:
#         if not(i.is() or i.islower()):
#             valid = False
#             break
#     if valid:
#         print("Correct")
#     else:
#         print("Incorrect")
# else:
#     print("Incorrect")


# s = input()
# allowed_letters = 'АВЕКМНОРСТУХ'
#
# if len(s) == 9:
#     if (s[0] in allowed_letters and
#         s[1].isdigit() and
#         s[2].isdigit() and
#         s[3].isdigit() and
#         s[4] in allowed_letters and
#         s[5] in allowed_letters and
#         s[6] == '_' and
#         s[7].isdigit() and
#         s[8].isdigit()):
#         print("YES")
#     else:
#         print("NO")
# elif len(s) == 10:
#     if (s[0] in allowed_letters and
#         s[1].isdigit() and
#         s[2].isdigit() and
#         s[3].isdigit() and
#         s[4] in allowed_letters and
#         s[5] in allowed_letters and
#         s[6] == '_' and
#         s[7].isdigit() and
#         s[8].isdigit() and
#         s[9].isdigit()):
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")


# n = int(input())
#
# comment = "COMMENT SHOULD BE DELETED"
#
# for i in range(1, n + 1):
#     s = input()
#     if s.isspace() or s == "":
#         print( i, ": ", comment, sep="")
#     else:
#         print(i, ": ", s, sep="")


# s1 = 'abc123'
# s2 = 'abc$*123'
# s3 = ''
#
# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())
