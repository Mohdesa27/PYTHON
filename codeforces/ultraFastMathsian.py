n=input()
m=input()
res=''
for i in range(len(n)):
    if (n[i]=='0' and m[i]=='1') or (n[i]=='1' and m[i]=='0'):
        res=res+'1'
    else:
        res=res+'0'
print(res)