from glob import glob
import spacy
from translate import eng2hin as translate

nlp = spacy.load("en_core_web_sm")

def sentence_seg(arg):
    temp = [sent.text for sent in arg.sents]
    return temp

path = glob("./files/*.mp4")[0] #to find "*.mp4" first file
name,_ = path.split(".mp4") #to remove extension
fileName = f"{name}.txt"

with open(fileName, "r") as rf:
    data = rf.read()
    data = nlp(data)

seg = sentence_seg(data)

def trans(args):
    dic = {}
    for eng in args:
        hin = translate(eng)
        dic.update({eng: hin})
    return dic

translated = trans(seg)

with open("./files/eng_and_hin.txt", "w", encoding="utf-8") as wf:
    wf.write(str(translated))