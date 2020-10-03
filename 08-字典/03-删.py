dict1 = {'name': 'tom', 'age': 20, 'gender': '男'}

# del 删除字典或指定的键值对
# del(dict1)
# print(dict1)

del (dict1['name'])
print(dict1)  # {'age': 20, 'gender': '男'}
# del(dict1['names']) 不存在报错


# clear
dict1.clear()
print(dict1)  # {}
