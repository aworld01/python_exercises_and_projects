"""
Byte rate:-
KB: 1024
MB: 1048576
GB: 1073741824
TB: 1099511627776
"""
# import os
# path = "Doctor.Strange.2016.1080p.Hindi.English.MoviesVerse.in.mkv"

# pro = os.stat(path)
# file_size = pro.st_size

def size(size, init="B"):
    factor = 1024
    l = ["", "K", "M", "G", "T", "P"]
    for unit in l:
        if size < factor:
            return (f"{round(size, 2)} {unit}{init}")
        size /= factor

data = size(1235345)
print(data)