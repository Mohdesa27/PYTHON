import os
directory = "making directory by mkdir"
parent_dir = "D:/ALLCODE/python/logical code/module/OS MODULE/"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
directory = "maked"
parent_dir = "D:/ALLCODE/python/logical code/module/OS MODULE/making directory by mkdir"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)
