"""
类属性的优点：
    类的实例 记录的某项数据 始终保持一致时，则定义类属性
    实例属性 要求每个对象 为其单独开辟一份内存空间来记录数据，
而类属性为全类所共有，仅占用一份内存，更加节省内存空间
"""


# 定义类
class Dog(object):
    # 定义类属性
    tooth = 10


wangcai = Dog()
xiaohei = Dog()

print(Dog.tooth)  # 10
print(wangcai.tooth)  # 10
print(xiaohei.tooth)  # 10

# 类属性只能通过类对象修改，不能通过实例对象修改
# 如果通过实例对象修改类属性，表示的是创建了一个实属性
Dog.tooth = 12
print(Dog.tooth)  # 12
print(wangcai.tooth)  # 12
print(xiaohei.tooth)  # 12

wangcai.tooth = 200
print(Dog.tooth)  # 12
print(wangcai.tooth)  # 200
print(xiaohei.tooth)  # 12
