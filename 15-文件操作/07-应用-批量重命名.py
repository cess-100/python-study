import os

flag = 1

file_list = os.listdir()

for name in file_list:
    if flag == 1:
        new_name = 'Python-' + name
    elif flag == 2:
        num = len('Python-')
        new_name = name[num:]
    os.rename(name, new_name)
