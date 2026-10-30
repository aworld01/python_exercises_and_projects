import os
from glob import iglob

flag = "*"
find = "pytorch"
replace = "PyTorch"
files = iglob(flag)

for file in files:
    temp = file.replace(find, replace)
    os.rename(file, temp)