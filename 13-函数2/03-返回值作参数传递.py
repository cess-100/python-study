def test1():
    return 50


def test2(num):
    print(num)


test2(test1())  # 50
