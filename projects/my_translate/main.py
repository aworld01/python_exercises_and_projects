import spacy
from source_code.gTrans import hindi
from source_code.strPro import sentence_tok, word_tok
from source_code.Json_dump import sentIntoJson, dictIntoJson
from source_code.trans_dbms import trans_search, dict_search, insert, delete

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
        if trans_search(i) == None:
            new_senten.append(i)
    return new_senten

def check_into_dict(arg):
    new_words = []
    for i in arg:
        if not i == trans_search:
            new_words.append(i)
    return new_words

print(check_into_trans(s))

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

# insert("I love my Dog.", "Main apne kutte se pyar karta hun")
# delete("I love my Cat")

# print(word)

# """save into json file"""
# dictIntoJson(word)
# sentIntoJson(senten)