# 在python中，值是靠引⽤用来传递来的

# 1. int类型  不可变类型
a = 1
b = a
print(b) # 1

print(id(a)) # 140733356696400
print(id(b)) # 140733356696400

a = 2
print(b) # 1

print(id(a)) # 140733356696432
print(id(b)) # 140733356696400


# 2.列表  可变类型
aa = [10, 20]
bb = aa

print(id(aa)) # 1884044944008
print(id(bb)) # 1884044944008

aa.append(30)
print(bb) # [10, 20, 30]

print(id(aa)) # 1884044944008
print(id(bb)) # 1884044944008
