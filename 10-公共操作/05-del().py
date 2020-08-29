str1 = 'abcdefg'
list1 = [10, 20, 30, 40, 50]
tuple1 = (100, 200, 300, 400)
set1 = {10, 20, 30, 40, 50}
dict1 = {'name': 'tom', 'age': 18}

# del 目标 或 del(目标)
del str1
# print(str1) NameError: name 'str1' is not defined

# del(list1)
# print(list1) NameError: name 'list1' is not defined

del(list1[0])
print(list1) # [20, 30, 40, 50]

# 元组不能删除元素
# del tuple1[0] TypeError: 'tuple' object doesn't support item deletion

del dict1['name']
print(dict1) # {'age': 18}