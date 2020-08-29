'''
1.准备数据
2.格式化输出数据
'''

age = 18
name = "tom"
weight = 75.5
stu_id = 1

print("今年我的年龄是%d岁" % age)
print("我的名字是%s" % name)
# %.2f，表示⼩小数点后显示的⼩小数位数
print("我的体重是%.1f公斤" % weight)
# %06d，表示输出的整数显示位数，不不⾜足以0补全，超出当前位数则原样输出
print("我的学号是%03d" % stu_id)

print("我的名字是%s，今年%d岁了" % (name, age))
print("我的名字是%s，今年%d岁了，体重%.1f公斤，学号是%06d" % (name, age, weight, stu_id))