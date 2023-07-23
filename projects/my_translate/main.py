import spacy
from source_code.gTrans import hindi
from source_code.strPro import sentence_tok, word_tok
from source_code.Json_dump import sentIntoJson, dictIntoJson
import source_code.trans_dbms as tra
import source_code.dict_dbms as dic

"""string processing"""
nlp = spacy.load("en_core_web_sm")
with open("demo.txt", 'r') as rf:
    data = rf.read()
    data = nlp(data)

s = sentence_tok(data)
w = word_tok(data)

def check_into_trans(arg):
    new_senten = []
    for i in arg:
        if tra.trans_search(i) == None:
            new_senten.append(i)
    return new_senten

def check_into_dict(arg):
    new_words = []
    for i in arg:
        if dic.dict_search(i) == None:
            new_words.append(i)
    return new_words

# print(check_into_trans(s))
print(check_into_dict(w))
# d1 = check_into_dict(w)

"""translate"""
def trans_data(a):
    sentences = {}
    for i in a:
        sentences.update({i:hindi(i)})
    return sentences


def dict_data(a):
    words = {}
    for i in a:
        words.update({i:hindi(i)})
    return words

# print(dict_data(d1))

# """save into json file"""
# dictIntoJson(dict_data(d1))
# sentIntoJson(dict_data(d1))