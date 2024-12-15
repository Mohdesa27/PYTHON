n=int(input("enter no. of value"))
value=[]
for i in range(n):
    value.insert(i,int(input()))
print(value)
sum=0
for i in range(n):
    sum=sum+value[i]
avg=sum//n
print(avg)
