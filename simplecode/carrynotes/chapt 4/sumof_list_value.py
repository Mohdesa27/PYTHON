n=int(input("enter the no of value"))
l=[]
sum=0
for i in range(n):
    a=int(input("enter the value"))
    l.append(a)
    sum=sum+l[i]
print(l)
print(sum)