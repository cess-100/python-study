"""
定义类
class 类名():
    代码
    ......
"""


class Washer(object):
    def wash(self):
        print('洗衣机洗衣服')
        print(self)


# 创建对象
# 对象名 = 类名()
haier1 = Washer()

# 打印haier1对象
# <__main__.Washer object at 0x000001A1D68AE780>
print(haier1)

# 使用功能
# 对象名.对象方法
# 洗衣机洗衣服
# <__main__.Washer object at 0x000002239A917438>
haier1.wash()


haier2 = Washer()

# <__main__.Washer object at 0x000001BB4CAEADA0>
print(haier2)

# 洗衣机洗衣服
# <__main__.Washer object at 0x000001BB4CAEADA0>
haier2.wash()
