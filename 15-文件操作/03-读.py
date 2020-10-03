# read() -- 文件对象.read(num)
# num表示要从文件中读取的数据的长度（单位是字节）
# 如果没有传入num，那么就表示读取文件中所有的数据
f = open('03test.txt', 'r')
# print(f.read())
print(f.read(10))
f.close()


# readlines()
# readlines按照行的方式把整个文件中的内容进行一次性读取
# 并且返回的是⼀个列表，其中每⼀行的数据为⼀个元素
f = open('03test.txt', 'r')
# ['aaaaa\n', 'bbbbb\n', 'ccccc\n', 'ddddd\n', 'eeeee']
print(f.readlines())
f.close()


# readline
# ⼀次读取⼀行内容
f = open('03test.txt', 'r')
print(f.readline())  # aaaaa 还有一个换行符
print(f.readline())  # bbbbb
f.close()
