"""
当程序执行到input ，等待用户输入，输入完成之后才继续向下执行。
在Python中， input 接收用户输⼊入后，一般存储到变量，方便使用。
在Python中， input 会把接收到的任意用户输入的数据都当做字符串处理。
"""

password = input('请输出您的密码：')
print('您输入的密码是%s' % password)
print(type(password))
