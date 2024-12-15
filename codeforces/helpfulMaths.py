a=input()
l=[]
for i in a.split('+'):
    l.append(i)
l.sort()
print('+'.join(l))