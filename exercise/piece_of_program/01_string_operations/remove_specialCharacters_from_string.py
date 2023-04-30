string = "Hello@# h%ow ar^e y*ou?"
special = "@#%^*"

for sp in special:
    string = string.replace(sp, "")
print(string)