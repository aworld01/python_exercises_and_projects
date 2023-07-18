import spacy
from source_code.gTrans import hindi
from source_code.strPro import sentence_tok, word_tok
from source_code.Json_dump import saveIntoJson

"""string processing"""
nlp = spacy.load("en_core_web_sm")
with open("demo.txt", 'r') as rf:
    data = rf.read()
    data = nlp(data)

s = sentence_tok(data)
w = word_tok(data)
# print(w)

"""translate"""
def trans_data(a,b):
    sentences = {}
    words = {}
    for i in a:
        sentences.update({i:hindi(i)})
    for i in b:
        words.update({i:hindi(i)})
    return sentences, words

senten, word = trans_data(s, w)
# saveIntoJson(senten, word)