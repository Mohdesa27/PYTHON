n=[2,4,5,8,7]
e=0
o=0
for i in n:
    if (i%2 == 0):
        print(n)
        e=e+1
    else:
        print(n)
        o=o+1
print("total even no:",e,"\n total of odd no:",o)