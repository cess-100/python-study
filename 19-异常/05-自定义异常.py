# 在Python中，抛出⾃定义异常的语法为raise 异常类对象
# 需求：密码⻓度不足，则报异常
# （用户输入密码，输⼊的长度不足3位报错，即抛出自定义异常，并捕获该异常）

class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f"你输入的长度是{self.length}, 不能少于{self.min_len}个字符"


def main():
    try:
        pwd = input('输入密码')
        if len(pwd) < 3:
            raise ShortInputError(len(pwd), 3)
    except Exception as e:
        print(e)
    else:
        print('密码输入完成')


main()
