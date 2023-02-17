import os
path = ('.')
n = os.listdir(path)


"""to access all files and dirs"""
print('All files and dirs.')
for file in n:
  print('\t',file)
print()
  

"""to access only file"""
# print('Only files')
# for file in n:
#   new = os.path.join(path, file)
#   if os.path.isfile(new):
#       print('\t',file)
# print()
  

"""to access only dir"""
# print('Only directories')
# for dir in n:
#   new = os.path.join(path, dir)
#   if os.path.isdir(new):
#       print('\t',dir)