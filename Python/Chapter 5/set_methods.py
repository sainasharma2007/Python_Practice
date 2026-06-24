#len()
s={1,34,65,2,879}
print(len(s))

# pop()
s={1,34,65,2,879}
print(s.pop())

# add()
s={1,34,65,2,879}
s.add(76)
print(s)

# difference()
s1={1,2,3}
s2={2,3,4}
s=s1-s2
print(s)

s1={1,2,3}
s2={2,3,4}
print(s2.difference(s1))

# remove()
s={1,34,65,2,879}
s.remove(34)
print(s)

# union()
s={1,2,3,4}
t={3,4,5,6}
print(s.union(t))

s={1,34,65,2,879}
print(s.union({879,43}))

# intersection()
s={1,2,3,4}
t={3,4,5,6}
print(s.intersection(t))

s={1,34,65,2,879}
print(s.intersection({879,43}))

# clear()
s={1,34,65,2,879}
print(s.clear())