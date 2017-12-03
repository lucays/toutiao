# 生成器表达式
nums = (i for i in range(100000))

lst = ['1', 1, '2', 2, 3, '3', 'a', 'str']
nums = (i for i in lst if isinstance(i, int))
print(nums)
for num in nums:
    print(num)

# 再次运行就不会产出任何值了。
for num in nums:
    print(num)

if nums:
    print('nums is not empty.')
