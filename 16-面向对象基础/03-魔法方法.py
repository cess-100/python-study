# __xx__() 函数叫做魔法方法，指的是具有特殊功能的函数

class Washer:
    def __init__(self, width, height):
        """定义初始化方法"""
        # 添加实例属性
        self.width = width
        self.height = height

    def __str__(self):
        return '这是海尔洗衣机的说明书'

    def __del__(self):
        print('对象已被删除')

    def wash(self):
        print('洗衣机洗衣服')

    def print_info(self):
        print('洗衣机的宽度是%d, 高度是%d' % (self.width, self.height))


haier1 = Washer(10, 20)  # 不传参数会报错
print(haier1)  # 这是海尔洗衣机的说明书
haier1.print_info()

haier1 = Washer(30, 40)
haier1.print_info()

"""
注意：
__init__() 在创建⼀个对象时默认被调用，不需要手动调用
__init__(self) 中的self参数，python解释器会自动把当前的对象引用传递过去

使用print输出对象，默认打印对象的内存地址
如果类定义了__str__ 方法，就会打印从在这个方法中return 的数据

删除对象时，python解释器会默认调用__del__() 方法。
"""
