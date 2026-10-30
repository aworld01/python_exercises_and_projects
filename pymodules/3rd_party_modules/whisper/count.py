from glob import glob
import spacy

special = [",","!","?",".",":",";"]

def sentence_seg(arg):
    temp = [sent.text for sent in arg.sents]
    return temp

def word_tok(arg):
    temp = [token.text for token in arg]
    return temp

def count_special(arg):
    w = []
    c = 0
    for i in special:
        if i in arg:
            c += 1
            w.append(i)
    return w, c

def removed_special(arg):
    w = []
    c = 0
    for i in arg:
        if i in special:
            continue
        else:
            w.append(i)
            c += 1
    return w,c

def unique(arg):
    u = sorted(set(arg))
    return u


"""read file"""
nlp = spacy.load("en_core_web_sm")

file = glob("*.txt")[0] #to find "*.mp4" first file

with open(file, 'r') as rf:
        data = rf.read()
        data = nlp(data)

seg = sentence_seg(data)
print(f"Sentanse: {len(seg)}")

all_words = word_tok(data)

print(f"Words: {len(all_words)}")

unique = unique(all_words)
print(f"Unque words: {len(unique)}")

words,count = count_special(all_words)
      
print(f"Special words: {words}")
print(f"special words count: {count}")

removed_words, removed_count = removed_special(all_words)
print(f"Filtered words: {removed_count}")