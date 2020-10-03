dict1 = {'name': 'tom', 'age': 20, 'gender': '男'}


# 遍历字典的key
for key in dict1.keys():
    print(key)


# 遍历字典的value
for value in dict1.values():
    print(value)


# 遍历字典的元素
for item in dict1.items():
    print(item, end=' ')  # ('name', 'tom') ('age', 20) ('gender', '男')


# 遍历字典的键值对
for key, value in dict1.items():
    print('%s = %s' % (key, value))
