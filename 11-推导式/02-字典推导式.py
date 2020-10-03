# 创建一个字典：key是1-5数字，value是这个数字的2次方
dict1 = {i: i ** 2 for i in range(1, 6)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 将两个列表合并为一个字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)  # {'name': 'Tom', 'age': 20, 'gender': 'man'}


# 提取上述电脑数量大于等于200的字典数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
dict3 = {key: value for key, value in counts.items() if value >= 200}
print(dict3)  # {'MBP': 268, 'DELL': 201}
