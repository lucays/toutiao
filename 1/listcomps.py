from time import clock

start = clock()

# 列表推导式
nums = [i for i in range(100000)]

end = clock()
print(end-start)

start_2 = clock()

# 普通的做法
nums = []
for i in range(100000):
    nums.append(i)

end_2 = clock()
print(end_2-start_2)

# 在列表推导式中使用if作条件过滤

lst = ['1', 1, '2', 2, 3, '3', 'a', 'str']
# 把不同类型的元素分开

nums = [i for i in lst if isinstance(i, int)]  # nums: [1, 2, 3]
print(nums)

s = [i for i in lst if isinstance(i, str)]  # s: ['1', '2', '3', 'a', 'str']
print(s)

# map(), filter()函数

