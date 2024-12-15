import os
directory = "making directory by makedirs"
parent_dir = "D:/ALLCODE/python/logical code/module/OS MODULE/"
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)
directory = "maked again"
parent_dir = "D:/ALLCODE/python/logical code/module/OS MODULE/making directory by makedirs"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path, mode)
print("Directory '% s' created" % directory)
