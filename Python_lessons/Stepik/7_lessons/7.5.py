number = int(input())

s = True
num = number % 10
while number != 0:
    num2 = number % 10
    if num2 < num:
        s = False
    else:
        num = num2
    number //= 10
if s == True:
    print("YES")
else:
    print("NO")






# number = int(input())
#
# num = number % 10
# num2 = 0
#
# while number != 0:
#     number_digit = number % 10
#     num2 = number_digit
#     if num != num2:
#         break
#     number //= 10
#
#
# if num == num2:
#     print("YES")
# else:
#     print("NO")



# number = int(input())
#
# digit = 0
#
# while number > 9:
#     twice_digit = number % 10
#     digit = twice_digit
#     number //= 10
# print(digit)


# number = int(input())
#
# temp = number
#
# amount = 0
# count = 0
# multiply = 1
# average = 0
# first_digit = 0
# amount_first_and_last = 0
#
# while temp != 0:
#     last_digit = temp % 10
#     amount += last_digit
#     count += 1
#     multiply *= last_digit
#     first_digit = last_digit
#     temp //= 10
#
# temp = number
#
# while temp != (temp % 10):
#     last_digit = temp % 10
#     amount_first_and_last = last_digit + first_digit
#     break
#
# print(amount, count, multiply, amount / count, first_digit, amount_first_and_last, sep="\n")

# number = int(input())
#
# count = str(number)
#
# print("Максимальная цифра равна", max(count),"\nМинимальная цифра равна", min(count))


# number = int(input())
#
# temp = number
# last = 0
# first = 9
#
# while temp != 0:
#     last_digit = temp % 10
#     if last_digit > last:
#         last = last_digit
#     temp //= 10
#
# temp = number
#
# while temp != 0:
#     first_digit = temp % 10
#     if first_digit < first:
#         first = first_digit
#     temp //= 10
#
# print("Максимальная цифра равна", last)
# print("Минимальная цифра равна", first)

# number = int(input())
#
# while number != 0:
#     last_digit = number % 10
#     number //= 10
#     print(last_digit, end="")

# number = int(input())
#
# while number != 0:
#     last_digit = number % 10
#     number //= 10
#     print(last_digit)


# number = int(input())
#
# has_7 = False
# count = 0
#
# while number != 0:
#     last_digit = number % 10
#     if last_digit == 7:
#         count += 1
#         has_7 = True
#     number //= 10
#
# if has_7 == True:
#     print(f"YES, count = {count}")
# else:
#     print("NO")


# number = int(input())
#
# while number != 0:
#     print(number)
#     last_digit = number % 10
#     number //= 10
#     print(last_digit)
