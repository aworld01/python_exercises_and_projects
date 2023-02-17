import os
path = '.'
n = os.listdir(path)
# skip = ".txt"
skip = ('.txt', '.py')

for file in n:
  if file.endswith(skip):
    continue
  print(file)
