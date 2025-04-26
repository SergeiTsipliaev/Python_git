



# import os
#
# abs_path = os.getcwd()
# file_name = 'data.json'
#
# print(os.path.join(abs_path, file_name))








# from os import write
# import json
#
# path = "data.json"
#
# json_data = {
#     'one': 'один',
#     'two': 'два',
#     'three': 'три',
#     'tour': 'четыре'
# }
#
# with open(path, "w", encoding="utf-8") as json_file:
#     json.dump(json_data, json_file, indent=4, ensure_ascii=False)
#
# with open(path, 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)
#
# print(data)






# from os import write
# import json
# path = "data.json"
#
# with open(path, "w", encoding="utf-8") as data_file:
#     # print(data_file.tell())
#
#     data = data_file.read()
#     print(data_file.seek(26))
#
# print(data)


# data = tuple(map(lambda x: x.strip(), data))


# with open(path, "w", encoding="utf-8") as data_file:





# path = "data.txt"
#
# with open(path, "r", encoding="utf-8") as data_file:
#     data = data_file.readlines()
#
# data = tuple(map(lambda x: x.strip(), data))
#
# with open(path, "w", encoding="utf-8") as data_file:
#     new_contact = "Ogan Simonan; 000; Spisok safer"
#     data_file.write("\n" + new_contact)

# "w" - write
# "a" - append - дописывает в конец файла инфу
# "r" - read
