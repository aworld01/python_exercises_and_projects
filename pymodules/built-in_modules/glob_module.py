import os
from glob import glob, iglob

# print(os.listdir())
# print()

# print(glob('*')) #to select all files and folders
# print()

# print(glob('test.txt')) #to select "test.txt"" file
# print()

# print(glob('*.txt')) #to select only txt file
# print()

# print(glob('??st.txt')) #it select file with two missing word
# print()

# print(glob("???????.py"))
# print()

# print(glob("[bg]*.*")) #select file which starts with "b" and "g"

# print(glob("[bn]*.py")) #to select file that matchs with 'b', 'n' as first charector and rest can be anything.
# print()

# print(glob("[!bn]*.py")) #This is opposite of above
# print()

# print(glob("**/*.py", recursive=True)) #to select all files recursively
# print()

# print(glob("**/*.py", recursive=True, include_hidden=True)) #to select all files recursively including hidden file also
# print()

globs = iglob("*") #it will return a generator
print(globs.__next__())
print(globs.__next__())

'''3:31/11:14'''