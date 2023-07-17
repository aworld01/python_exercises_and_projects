import os

"""split file name to save txt file with file name"""
file = "Search Engine Using Javascript And HTML Simple Tutorial(720P_60FPS).mp4"
file_name, _ = os.path.splitext(file)

print(file)
print()
print(file_name)