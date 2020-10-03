a = 'hello ' \
    'world'
print(type(a))
print(a)
# hello world

b = "to" \
    "m"
print(type(b))
print(b)
# tom

# 三引号 支持回车换行
c = '''i am tom'''
print(type(c))

d = """i 
am tom"""
print(type(d))
print(d)
# i
# am tom

# I'm tom
f = "I'm tom"
print(type(f))
print(f)  # I'm tom

# f = 'I'm tom' ❌
f = 'I\'m tom'
