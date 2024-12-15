def func(n):
    return abs(n-30)
n=int(input("enter the value of n="))
x=func(n)
print(x)
thislist = [100, 50, 65, 82, 23,30]
thislist.sort(key = func)#where key is work as dictionary:{100:70,50:20,65:35,82:52,23:7,30:0}
print(thislist)#then sort list according to given output from function
#[0:30,7:23,20:50,35:65,70:100]