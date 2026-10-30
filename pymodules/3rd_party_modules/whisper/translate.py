#pip install googletrans==4.0.0-rc1  (solved)

from googletrans import Translator

def eng2hin(query):
    gt = Translator()
    t = gt.translate(query, dest="hi")
    return t.text



if __name__ == "__main__":
    s2 = "hello there"
    print(eng2hin(s2))