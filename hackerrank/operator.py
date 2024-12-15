# a = int(input())
# b = int(input())
# print(a//b)
# print(a/b)

# 
# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# year = 1990
# print(is_leap(year))  # Output True or False

n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
    print(i,end="")

n = int(input())
print("".join(str(i) for i in range(1, n + 1)))

