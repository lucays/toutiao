def func(a, b):
    a += b
    return a


a, b = 1, 2
func(a, b)
# print(a, b)

a, b = (1, 1), (2, 2)
func(a, b)
# print(a, b)

a, b = [1, 1], [2, 2]
func(a, b)
# print(a, b)


def func(lst=[]):
    lst.append('test')
    return lst


a = func()
print('a', a)
b = func()
print('b', b)
c = [1, 2]
d = func(c)
print('d', d)
e = func(d)
print('e', e)

print('a', a)
print('b', b)
print('d', d)
print('e', e)
print('c', c)


def func(lst=None):
    if lst is None:
        lst = []
    lst.append('test')
    return lst


a = func()
print('a', a)
b = func()
print('b', b)
c = [1, 2]
d = func(c)
print('d', d)
e = func(d)
print('e', e)

print('a', a)
print('b', b)
print('d', d)
print('e', e)
print('c', c)


def func(lst=None):
    if lst is None:
        lst = []
    else:
        lst = list(lst)
    lst.append('test')
    return lst


a = func()
print('a', a)
b = func()
print('b', b)
c = [1, 2]
d = func(c)
print('d', d)
e = func(d)
print('e', e)

print('a', a)
print('b', b)
print('d', d)
print('e', e)
print('c', c)
