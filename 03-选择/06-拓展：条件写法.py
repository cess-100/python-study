age = int(input('请输入您的年龄：'))
if age < 16:
    print(f'您输入的年龄是{age}，童工')
elif 16 <= age < 65:
    print(f'您输入的年龄是{age}，合法')
else:
    print(f'您输入的年龄是{age}，退休年龄')