t1 = (1, 2, [3, 4])
id1 = id(t1[2])
t1[2].append(5)
id2 = id(t1[2])
print(t1)
print(id1 == id2)
