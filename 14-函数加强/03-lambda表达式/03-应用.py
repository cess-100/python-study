# 带判断的lambda
print((lambda a, b: a if a > b else b)(1000, 500))

#
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# 按name值升序排列
students.sort(key=lambda x: x['name'])
print(students)

# 按name值降序排列列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)

# 按age值升序排列列
students.sort(key=lambda x: x['age'])
print(students)
