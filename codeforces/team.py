n=int(input())
l=list()
for i in range(n):
    l.append(input())
lres=0
for i in l:
    if(l[0]==l[2] or l[0]==l[4] or l[2]==l[4]) and ((l[0]=='1' and l[2]=='1') or( l[0]=='1'and l[4]=='1') or( l[2]=='1' and l[4]=='1')):
        
        lres+=1
print(lres)