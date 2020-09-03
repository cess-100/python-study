"""
静态方法特点:
需要通过装饰器@staticmethod 来进行修饰，
静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）。
静态方法也能够通过实例对象和类对象去访问
"""


class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个狗类，用于创建狗实例....')


wangcai = Dog()
Dog.info_print()
wangcai.info_print()
