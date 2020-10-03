# 1.位置参数
# 注意：传递和定义参数的顺序及个数必须一致
def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄{age}, 性别{gender}')


user_info('TOM', 20, '男')


# 2.关键字参数
# 注意：函数调用时，如果有位置参数，位置参数必须在关键字参数的前面，
# 但关键字参数之间不存在先后顺序
def user_info2(name, age, gender):
    print(f'您的名字是{name}, 年龄{age}, 性别{gender}')


user_info2('Rose', age=18, gender='女')
user_info2('小明', gender='男', age=16)
# user_info2(gender='男', age=16. '小明') 报错


# 3.缺省参数
# 注意：函数调用时，有缺省参数则使用缺省参数，否则使用默认值
def user_info3(name, age, gender='男'):
    print(f'您的名字是{name}, 年龄{age}, 性别{gender}')


user_info3('TOM', 20)  # 您的名字是TOM, 年龄20, 性别男
user_info3('Rose', 18, '女')


# 4.可变参数
# 可传可不传数据

# 包裹位置传递
# 注意：所有参数都会被args变量收集，会根据参数的位置合并为⼀个元组(tuple)，
def user_info4(*args):
    print(args)


user_info4('TOM')  # ('TOM',)
user_info4('TOM', 18)  # ('TOM', 18)


# 包裹关键字传递
# 返回的是一个字典dict
def user_info5(**kwargs):
    print(kwargs)


user_info5(name='TOM', age=18, id=110)  # {'name': 'TOM', 'age': 18, 'id': 110}

# 综上：⽆论是包裹位置传递还是包裹关键字传递，都是⼀个组包的过程
