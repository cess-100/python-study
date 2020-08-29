str1 = 'abcd'
list1 = [10, 20, 30, 40]
tuple1 = (100, 200, 300, 400)
dict1 = {'name': 'python', 'age': 30}

print('a' in str1) # True
print('a' not in str1) # False

print(10 in list1) # True
print(10 not in list1) # False

print(100 in tuple1) # True
print(100 not in tuple1) # False

print('name' in dict1) # True
print('name' not in dict1) # False
print('name' in dict1.keys()) # True
print('name' in dict1.values()) # False
