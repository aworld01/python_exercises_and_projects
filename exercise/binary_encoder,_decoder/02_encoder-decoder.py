usr_inp = input("Enter your data: ")

"""encoder"""
num = [format(ord(i),"b") for i in usr_inp]
# print(num)

num = " ".join(num)
print(num)
print()


"""decoder"""
"""example1"""
# string = [int(i,2) for i in num.split()]
# print(string)

"""example2"""
string = [chr(int(i,2)) for i in num.split()]
# print(string)

string = "".join(string)
print(string)