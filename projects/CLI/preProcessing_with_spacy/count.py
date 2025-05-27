import spacy


special = [",","!"]

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

with open("temp.txt", 'r') as rf:
        data = rf.read()
        data = nlp(data)
print(data)
print()

all_words = word_tok(data)
print(all_words)

print(f"All words count: {len(all_words)}")
print()

unique = unique(all_words)
print(f"Unique words: {unique}")
print(f"Length of unque words: {len(unique)}")
print()

words,count = count_special(all_words)
      
print(f"Special words: {words}")
print(f"special words count: {count}")
print()

removed_words, removed_count = removed_special(all_words)
print(f"Filtered words: {removed_words}")
print(f"Filtered words count: {removed_count}")
print()

seg = sentence_seg(data)
print(seg)
seg_count = len(seg)
print(f"Sentanse count: {seg_count}")