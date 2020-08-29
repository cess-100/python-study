dict1 = {'name':'tom', 'age':20, 'gender':'男'}

# 写法：字典序列[key] = 值
# 如果key存在则修改这个key对应的值；如果key不存在则新增此键值对

dict1['id'] = 110
print(dict1) # {'name': 'tom', 'age': 20, 'gender': '男', 'id': 110}

dict1['name'] = 'rose'
print(dict1) # {'name': 'rose', 'age': 20, 'gender': '男', 'id': 110}