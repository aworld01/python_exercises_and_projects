
from googletrans import Translator

def translator(query):
    gt=Translator()
    t=gt.translate(query, dest="hi")
    data=t.text
    return data

if __name__ == "__main__":
    query = "my name is abdul zoha"
    dic = {}
    dic.update({query:translator(query)})
    print(dic)