# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)


# 徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
        # self.money = 2000000
        # 定义私有属性
        self.__money = 2000000

    # get 获取私有属性
    def get_money(self):
        return self.__money

    # set 设置私有属性
    def set_money(self, money):
        self.__money = money

    # 定义私有方法
    def __info_print(self):
        print(self.kongfu)
        print(self.__money)

    def make_cake(self):
        self.__init__()
        print('使用%s制作煎饼果子' % self.kongfu)

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 徒孙类
class Tusun(Prentice):
    pass


daqiu = Prentice()
# daqiu.__info_print() 无法访问私有方法
daqiu._Prentice__info_print()


xiaoqiu = Tusun()
print(xiaoqiu.get_money())
xiaoqiu.set_money(500)
print(xiaoqiu.get_money())

# print(xiaoqiu.__money) 无法访问私有属性
print(xiaoqiu._Prentice__money)
# xiaoqiu.__info_print() 无法访问私有方法
xiaoqiu._Prentice__info_print()

"""
注意：
私有属性和私有方法非特殊手段，只能在类里面访问和修改
一般定义函数名get_xx 用来获取私有属性，定义set_xx 用来修改私有属性值
"""
