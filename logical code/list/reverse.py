a=[]
n=int(input("enter the no of element"))
for i in range(0,n):
    x=int(input("enter the element"))
    a.append(x)
l=n-1
for i in range(0,n//2):
    a[i],a[l]=a[l],a[i]
    l=l-1
print("reverse list is")
print(a)    