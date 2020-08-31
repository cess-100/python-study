# 无参数
fn1 = lambda: 100
print(fn1())

# 一个参数
fn2 = lambda a: a
print(fn2('hello world'))

# 默认参数
fn3 = lambda a, b, c=100: a + b + c
print(fn3(10, 20))
print(fn3(10, 20, 30))

# 可变参数 *args
fn4 = lambda *args: args
print(fn4(10, 20, 30))

# 可变参数 **kwargs
fn5 = lambda **kwargs: kwargs
print(fn5(name='python', age=20))
