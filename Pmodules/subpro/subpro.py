import subprocess

# subprocess.run('ls') #to run a simple command

# subprocess.run('ls -la', shell=True) #to run command with arguments

# subprocess.run(['ls', '-la']) #to run command with arguments

# comm = 'ls -la'
# comm = comm.split() #to convert into list
# # print(comm)
# subprocess.run(comm)




# comm = "ls -la"
# p1 = subprocess.run(comm, shell=True)
# print(p1)
# print(p1.args)
# print(p1.returncode)
# print(p1.stdout)


"""example-1"""
"""
stdout=subprocess.PIPE == capture_output=True
"""
# p1 = subprocess.run("ls -l", shell=True, capture_output=True) #capture_output=True (returns output in binary form)
# print(p1)


"""example-2"""
# p1 = subprocess.run("ls -l", shell=True, stdout=subprocess.PIPE) #stdout=subprocess.PIPE (returns output in binary form)
# print(p1)


# p1 = subprocess.run("ls -l", shell=True, capture_output=True)
# print(p1.stdout.decode()) #stdout.decode() converts binary into text


# with open('outPut.txt', 'w') as wf:
#     p1 = subprocess.run("ls -l", shell=True, stdout=wf, text=True) #to save output into text