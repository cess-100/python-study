name_list = ['tom', 'lily', 'rose']

# copy 复制
list1 = name_list.copy()
print(list1)  # ['tom', 'lily', 'rose']

name_list[0] = 'aaa'
print(name_list)  # ['aaa', 'lily', 'rose']
print(list1)  # ['tom', 'lily', 'rose']
