# 1. 定义全局变量量
glo_num = 0

def test1():
    global glo_num
    # 修改全局变量量
    glo_num = 100

def test2():
    # 调⽤用test1函数中修改后的全局变量量
    print(glo_num)

test2() # 0
test1()
test2() # 100
