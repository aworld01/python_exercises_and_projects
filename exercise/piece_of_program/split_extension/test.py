import os

file = "synonymous.words.txt"
print(f"The original file is: {file}")
print()

file_name, extension = os.path.splitext(file)
print(f"The file name is: {file_name}")
print(f"And the extension is: {extension}")