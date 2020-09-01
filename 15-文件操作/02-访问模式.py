"""
1.测试目标：访问模式对文件的影响
2.访问模式对write()的影响
3.访问模式是否可以省略
"""

# r
# f = open('test1.txt', 'r') # 如果文件不存在，报错
f = open('03test.txt', 'r')
# f.write('aa') # 不支持写入，报错 not writable
f.close()


# w
f = open('1.txt', 'w') # 如果文件不存在，新建文件
f.write('bbb') # 写入会覆盖原有内容
f.close()


# a
f = open('2.txt', 'a') # 如果文件不存在，新建文件
f.write('xyz') # 写入会不会覆盖原有内容，而是追加
f.close()


# 访问模式是否可以省略
# 默认是访问模式是r
f = open('3.txt')
f.close()


"""
r   rb  r+  rb+ 
w   wb  w+  wb+
a   ab  a+  ab+
凡是b就是二进制格式打开，凡是+可读可写
r一行不会新建文件，没有就报错，指针在开头
w一行没有就新建，w模式先清空再写⼊，指针在开头
a一行没有就新建，a模式直接末尾追加，指针在结尾
"""