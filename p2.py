SetA = set(map(int, input().split()))
SetB = set (map(int,input ().split()))

u1 = SetA .union(SetB)
i2 = SetA .intersection(SetB)
d3 = SetA .difference(SetB)

print("union ",u1,"intersection",i2,"differenc",d3)
