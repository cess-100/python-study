"""
while 条件:
    条件成⽴立重复执⾏行行的代码
else:
    循环正常结束之后要执⾏行行的代码
"""
# while else  和for  else
# 意思就是while是和else一块的
# 当有break或者return的时候，会跳出while块
# 又因为while和else是一个整体，所以就跳出else，就不执行else
# 所以只要没有break或者return，不管while是否执行，都会执行else语句（continue也是可以执行else）

# 连续说5遍“媳妇儿，我错了”，如果道歉正常完毕女朋友就原谅我了
i = 1
while i <= 5:
    print("媳妇儿，我错了")
    i += 1
else:
    print("女朋友就原谅我了")