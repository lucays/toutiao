import timeit

TIMES = 10000

SETUP = """
data = ['30', 50, 91.1]*1000
"""

foo = '''
s = 0
for p in data:
    s += int(p)
'''


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))


clock('for +=         :', foo)
clock('generator sum  :', 'sum(int(i) for i in data)')
clock('list sum       :', 'sum([int(i) for i in data])')
