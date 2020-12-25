# seek -- 文件对象.seek(偏移量, 起始位置)
"""
起始位置：
    0：文件开头
    1：当前位置
    2：文件结尾

python3偏移量没有使用b模式打开不能为负
单r模式起始位置不能为1
"""

# f = open('03test.txt', 'r+')
f = open('03test.txt', 'a+')

# 改变读取开始位置
f.seek(2, 0)
# f.seek(0, 1)
print(f.read())

# 另外 tell() 返回当前指针位置
print(f.tell())
f.close()

