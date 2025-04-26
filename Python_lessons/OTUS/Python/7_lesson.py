

def hello_decorator(func):

    def inner(*args, **kwargs):
        print('Hello')
        func()
        print('Goodby')
    return inner

@hello_decorator
def print_info():
    print('Something')


print_info()
print_info()
print_info()





# from random import randint
# from  string import ascii_lowercase


# def func():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6
#     yield 7
#
# a = func()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# def create_name():
#     name = ""
#     for _ in range(randint(5, 10)):
#         name += ascii_lowercase[randint(0, len(ascii_lowercase) - 1)]
#     return name.title()
#
# names = (create_name() for _ in range(15))
#
# for i in names:
#     print(i)
