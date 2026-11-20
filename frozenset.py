fs=frozenset([1,2,3])
print(fs)

#frozen set as dictionary key
fs = frozenset([1, 2, 3])
d = {fs: "numbers"}
print(d)

#methods in frozenset
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))