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

nums = [i for i in lst if isinstance(i, int)]  # nums: [1, 2, 3]
print(nums)

s = [i for i in lst if isinstance(i, str)]  # s: ['1', '2', '3', 'a', 'str']
print(s)

# filter()函数
nums = list(filter(lambda x: isinstance(x, int), lst))  # nums: [1, 2, 3]
print(nums)

# 嵌套循环
colors = ['black', 'white']
sizes = ['L', 'XL']
# pants: [('black', 'L'), ('black', 'XL'), ('white', 'L'), ('white', 'XL')]
pants = [(color, size) for color in colors for size in sizes]
print(pants)

# 上下文的同名变量
x = 'mydata'
nums = [x for x in lst if isinstance(x, int)]
print(x)
