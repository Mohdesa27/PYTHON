with open("index.txt","r") as f:
    print(f.tell())
    f.seek(3)
    print(f.read(5))
    f.seek(0,2)
    l=f.tell()
    print("size of file",l)
    f.seek(-3,2)
    x=f.read(3)
    print(x)
    