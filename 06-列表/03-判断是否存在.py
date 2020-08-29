name_list = ['tom', 'lily', 'rose']

# in
print('tom' in name_list) # True
print('toms' in name_list) # False

# not in
print('tom' not in name_list) # False
print('toms' not in name_list) # True


# 需求：注册邮箱，根据输入判断账号是否存在
name = input('请输入您的邮箱账号名：')

if name in name_list:
    # 提示用户名存在
    print(f'您输入的名字是{name}, 此用户名已存在')
else:
    # 提示可以注册
    print(f'您输入的名字是{name}, 此用户名可以注册')
