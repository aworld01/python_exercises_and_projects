import os

def exst(item):
    if not os.path.exists(item):
        os.makedirs(item)

exst('my_folder')
