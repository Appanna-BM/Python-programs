s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

s = {10, 20, 30}
#s.remove(40)    # Error because 40 doesn't exist
#print(s)

s.pop()
print(s)

s.add(50)
print(s)

s.update([60,70])
print(s)

s.discard(40)   # No error
print(s)

