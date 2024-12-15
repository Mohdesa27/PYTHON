x=int(input())
y=int(input())
z=int(input())
n=int(input())
print([(i,j,k) for i in range(x) 
                        for j in range(y)
                        for k in range(z)
                        if i+j+k !=n])
# Input the dimensions and the integer n
# length = int(input("Enter the length of the cuboid: "))
# width = int(input("Enter the width of the cuboid: "))
# height = int(input("Enter the height of the cuboid: "))
# n = int(input("Enter the integer n: "))

# # Generate the list of coordinates using list comprehension
# coordinates = [(x, y, z) for x in range(length) 
#                                for y in range(width) 
#                                for z in range(height) 
#                                if x + y + z != n]

# Print the list of coordinates
#print(coordinates)
