lst = ['a', 'b', 'c', 1, 2, 3, 'b', 2, 4]
nums = {i for i in lst if isinstance(i, int)}
print(nums)  # {1, 2, 3, 4}
