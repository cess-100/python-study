# 需求：有三个办公室，8位老师，8位老师随机分配到3个办公室

import random

teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

for name in teachers:
    offices[random.randint(0, 2)].append(name)

i = 1
for office in offices:
    print("办公室%d老师人数为%d，老师分别是：" % (i, len(office)), end='')
    i += 1
    for name in office:
        print(name, end=" ")
    print()
