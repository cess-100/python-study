# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)


# 徒弟类
class Prentice(Master):
    pass


daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

# 类名.__mro__  查看继承顺序
# (<class '__main__.Prentice'>, <class '__main__.Master'>, <class 'object'>)
print(Prentice.__mro__)
