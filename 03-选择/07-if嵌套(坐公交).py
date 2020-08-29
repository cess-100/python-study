"""
1. 如果有钱，则可以上⻋车
2. 上⻋车后，如果有空座，可以坐下
上⻋车后，如果没有空座，则站着等空座位
如果没钱，不不能上⻋车
"""
# 假设⽤用 money = 1 表示有钱, money = 0表示没有钱;
# seat = 1 表示有空座，seat = 0 表示没有空座
money = 1
seat = 0

if money == 1:
    print('土豪请上车', end='')
    if seat == 1:
        print('，有座位坐下')
    else:
        print('，没座位站着')
else:
    print('没钱跟着跑')