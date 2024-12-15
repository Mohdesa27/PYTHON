f=open("index.txt","r")
text=f.readline()
print(text)
f.close()

f=open("index.txt","r")
text=f.readlines()
print(text)
f.close()