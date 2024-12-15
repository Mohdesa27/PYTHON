n=int(input("enter the no"))
e=0
o=0
while n>0:
    r=n%10
    if r%2==0:
        e=e+1
    else:
        o=o+1
    n=n//10
print("total even no:",e,"\n total of odd no:",o)