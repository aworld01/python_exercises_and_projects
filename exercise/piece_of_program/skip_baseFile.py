import os
path = '.'
n = os.listdir(path)
n.remove('skip_baseFile.py')

for file in n:
  print(file)