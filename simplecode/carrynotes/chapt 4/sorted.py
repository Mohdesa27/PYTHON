n=int(input("enter the no. of student"))
l=[]
for i in range(n):
    marks=int(input("enter the marks"))
    l.append(marks)
    l.sort()
print(l)