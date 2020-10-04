# else表示的是如果没有异常要执行的代码
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，是没有异常的时候执⾏行行的代码')
