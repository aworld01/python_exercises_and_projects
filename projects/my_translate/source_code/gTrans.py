"""
pip install googletrans #to install googletrans
pip install googletrans==4.0.0-rc1  (solved)
"""

from googletrans import Translator

def english(query):
    gt = Translator()
    t = gt.translate(query)
    data = t.text
    return data

def hindi(query):
    gt = Translator()
    t = gt.translate(query, src="en", dest="hi")
    d = t.text
    return d

if __name__ == "__main__":
    query = "मेरा नाम एलेक्सा है"
    query2 = "hello there"

    hin = hindi(query2)
    print(hin)