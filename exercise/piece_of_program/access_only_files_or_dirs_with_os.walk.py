import os
source = ('.')

# for path, folders, files in os.walk(source):
#   for file in files:
#     print(file)
# print()

for path, folders, files in os.walk(source):
  for folder in folders:
    print(folder)