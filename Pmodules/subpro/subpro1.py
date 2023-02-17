import os
import subprocess

"""
cmd = "ls -lrt"

cmd = cmd.split() #use instead using shell=False

sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #gives output as binary

sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) #gives output as string

rs = sp.wait() #wait till execute the commands

stdout=subprocess.PIPE #returns output

stderr=subprocess.PIPE #returns error

universal_newlines=True #gives output as string

out.splitlines() #to convert lines into list

shell=True/False
shell = True (commands = string)
shell = False (commands = list)
"""
cmd = "ls -lrt"

sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) #gives output as string

rc = sp.wait()
out, err = sp.communicate()
print(f"The return code is: {rc}")
print(f"The output is: {out}")
print(f"The error is: {err}")




# file = subprocess.Popen("mousepad") #to open file

# file = subprocess.Popen(["mousepad", "myFile"]) #to open file with file name


# file = subprocess.Popen(["mousepad", "myFile"]) #to open file with file name
# usr_inp = input("Type exit to exit: ")
# if usr_inp == "exit":
#     file.terminate()


# browser = subprocess.Popen("/bin/firefox")


# browser = subprocess.Popen(["/bin/firefox", "www.facebook.com"])