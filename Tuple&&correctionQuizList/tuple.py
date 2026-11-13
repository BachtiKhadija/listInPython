t=tuple(x for x in range(20))
print(t)
print(type(t))
print(t[2])
#t[3]=100
l=list(t)

l[3]=100
t=tuple(l)
print(t)