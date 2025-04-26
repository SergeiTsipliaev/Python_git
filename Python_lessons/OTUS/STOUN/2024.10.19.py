import os

def rename_files(path: str):
    files_list = os.listdir(path)
    for file in files_list:
        file_name = (file[0:-5])
        new_file_name = []
        word = ''
        for ch in file_name:
            if ch.isalpha() or ch.isdigit():
                word += ch()
            else:
                new_file_name.append(word)
                word = ''

        print(new_file_name)


rename_files(r'/Users/mbp162021m1pro/Desktop/Примеры работ')