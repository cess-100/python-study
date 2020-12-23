"""
提示：0-石头，1-剪刀，2-布
1. 出拳
    玩家输入出拳
    电脑随机出拳
2. 判断输赢
    玩家获胜
    平局
    电脑获胜
"""

import random

# 1. 出拳
# 玩家
player = int(input('请出拳：0-石头，1-剪刀，2-布'))
# 电脑
computer = random.randint(0, 2)
print('电脑出%d' % computer)

# 2.判断输赢
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
