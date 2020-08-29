age = int(input('请输入你的年龄：'))
if age >= 18:
    print('您输入的年龄是%d，已经成年，可以上网' % age)
else:
    print(f'您输入的年龄是{age}，未成年，不可以上网')
print('系统关闭')