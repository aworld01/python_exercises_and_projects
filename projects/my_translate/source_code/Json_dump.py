import json

def saveIntoJson(dic, sen):
    with open("dict.json", "w") as wf:
        json.dump(dic, wf, indent=4) #to give indent of 4 spaces
    with open("tran.json", "w"):
        json.dump(sen, wf, indent=4)

if __name__ == "__main__":
    list_data = ["Apple", "Orange", "Banana", "Guava"]
    dict_data = {"name":"Abdul Zoha", "age":25, "skills":["python", "shell", "javaScript"], "Yes":True, "No":False}