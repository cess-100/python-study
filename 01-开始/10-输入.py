'''
当程序执⾏行行到input ，等待⽤用户输⼊入，输⼊入完成之后才继续向下执⾏行行。
在Python中， input 接收⽤用户输⼊入后，⼀一般存储到变量量，⽅方便便使⽤用。
在Python中， input 会把接收到的任意⽤用户输⼊入的数据都当做字符串串处理理。
'''

password = input('请输出您的密码：')
print('您输入的密码是%s' % (password))
print(type(password))
