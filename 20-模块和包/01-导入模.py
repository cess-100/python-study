"""
模块(Module)，是一个Python 文件，以.py 结尾，包含了Python 对象定义和Python语句
模块能定义函数，类和变量，模块里也能包含可执行的代码
"""

"""
# 1. 导⼊入模块
    import 模块名
    import 模块名1, 模块名2...  （不推荐）
# 2. 调⽤用功能
    模块名.功能名()
"""

import math
print(math.sqrt(9))  # 3.0


"""
from 模块名 import 功能1, 功能2, 功能3...
"""

from math import sqrt
# 不再需要前面写模块名.方法
print(sqrt(9))


"""
from 模块名 import *
"""

from math import *
print(sqrt(9))
