import json

def dictIntoJson(arg):
    with open("source_code/dict.json", "w", encoding="utf-8") as wf:
        json.dump(arg, wf, indent=4, ensure_ascii=False)
def sentIntoJson(arg):
    with open("source_code/sent.json", "w", encoding="utf-8") as wf:
        json.dump(arg, wf, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    data = {"My name is Alexa":"मेरा नाम एलेक्सा है"}
    list_data = ["Apple", "Orange", "Banana", "Guava"]
    dict_data = {"name":"Abdul Zoha", "age":25, "skills":["python", "shell", "javaScript"], "Yes":True, "No":False}
    dictIntoJson(data)