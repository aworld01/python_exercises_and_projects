find = "Abdul Zoha"
replace = "world"
file = "data.txt"

with open(file, mode='r') as rf:
  found = rf.read()
  replaced = found.replace(find, replace)
  with open(file, mode='w') as wf:
    wf.write(replaced)