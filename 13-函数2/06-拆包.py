# 拆包：元组
def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1)  # 100
print(num2)  # 200

# 拆包：字典
dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1

# 对字典进⾏行行拆包，取出来的是字典的key
print(a)  # name
print(b)  # age
print(dict1[a])  # TOM
print(dict1[b])  # 18
