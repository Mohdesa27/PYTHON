a=[1,6,8,3,9,4,6,6]
for i in range(0,9):
    x=a.count(6)
print(x)
for i in range(0,x):
    a.remove(6)
print(a)