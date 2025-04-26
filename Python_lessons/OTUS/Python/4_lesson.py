# my_list = list("ABCDEF")

# print(my_list)

# for i in range(len(my_list)):
#     if my_list[i] == "C":
#         my_list[i] = "AAA"

# print(my_list)

# //////////////////
# from itertools import count
#
# my_list = list("abcdef")
# my_tuple = tuple(my_list)
# my_set = set(my_list)
# # my_dict = dict.fromkeys(my_tuple, None)
# my_dict = dict.fromkeys(my_tuple, None)
#
# # for collection in (my_list, my_tuple, my_set, my_dict):
# #
# #     print(collection)
# #     print(type(collection))
# #     print()
#
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
# //////////////////


# !!!!!!!!!DICT!!!!!!!!!!!

# my_dict = {"one": 1, "two": 3, "three": 3}
# new_dict = {"thb": 333, "five": 5}
#
# # print(my_dict.popitem())
# # print(my_dict.setdefault("twice", 333))
# dict_2 = {}.fromkeys("abcdef", None)
# print(my_dict)
# print(dict_2)


# my_dict = {"one": 1, "two": 3, "three": 3}
# new_dict = {"thb": 333, "five": 5}
#
# my_dict.update(new_dict)
# print(my_dict)


# my_dict = {"one": 1, "two": 3, "three": 3}
#
# my_dict["four"] = 4
#
# print(my_dict)
# print(my_dict["four"])
# print(my_dict.get("fou", "None"))
# print(my_dict.pop("two"))
# print(my_dict)


# !!!!!!!!!SET!!!!!!!!!!!

# set_a = {1,2,3}
# set_b = {3,4,5}
# set_a.intersection_update(set_b)
# print(set_a)

# set_one = {1,2,3}
# set_two = {3,4,5}
#
# print(set_one.union(set_two))


# set_one = {1,2,3}
# set_two = {3,4,5}
#
# d_set = set_one.difference(set_two)
# print(set_one.difference(set_two))
# print(d_set)
# print(set_one.intersection(set_two))


# my_set = {"1","2","3","4","5"}
# my_set1 = {1,2,3,4,5}
# my_set2 = [1,2,3,4,5,5,5,5,5,5,5]
# my_set2 = list(set(my_set2))#удаляем дубликаты и приводим к set при этом теряется порядок
#
# print(my_set)
# print(my_set1)
# print(my_set2)


# !!!!!!!!!TUPLE!!!!!!!!!!!
# my_tuple = (1,)
# print(my_tuple[0])


# my_tuple = (1, 2, 3, 4, 5, 5)
# print(my_tuple.count(5))
# print(my_tuple.index(2))
# print(my_tuple[3])

# !!!!!!!!!LIST!!!!!!!!!!!
# from copy import deepcopy
#
# a = ["a", "t", "b", "c", "d",[1, 2]]
#
# b = deepcopy(a)
# print(a)
# print(b)
# b[-1][123:] = ["HJD", 123]
# print(a)
# print(b)


# a = ["a", "t", "b", "c", "d",[1, 2]]

# b = a.copy()
# print(a)
# print(b)
# a[-1].append(input("GO"))
# print(a)
# print(b)

# a = ["a", "t", "b", "c", "d"]
#
# a.sort(reverse=True)
# print(a)


# a = [1,2,3,4,5,4,4]
#
# a.insert(1, 123)
# a.remove(123)
# b = a.pop(4)
#
# print(a)
# print(b)


# a = [1, 2, 3, 4]

# a[0] = ("1, 3, 4, 1, 8, 8")

# print(a)


# my_list = [1, 2, 3, "sd", True, "3"]
#
# print(my_list[1:4])


# list = список
# tuple = кортеж
# set = множество
# dict = словарь
