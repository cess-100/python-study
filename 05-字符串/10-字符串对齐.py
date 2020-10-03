mystr = 'hello'

# 1.ljust() 左对齐
print(mystr.ljust(10))  # 'hello     '
print(mystr.ljust(10, '*'))  # hello*****

# 2.rjust() 左对齐
print(mystr.rjust(10, '*'))  # *****hello

# 3.center() 左对齐
print(mystr.center(10, '*'))  # **hello***
