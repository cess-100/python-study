# input接受用户输入的数据是字符串类型
# 条件是age和整型18做判断，所以这⾥里要int转换数据类型
age = int(input('请输入您的年龄：'))

if age >= 18:
    print(f'您的年龄是{age},已经成年，可以上网')
print('系统关闭')
