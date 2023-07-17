import spacy

nlp = spacy.load("en_core_web_sm")

with open("demo.txt", 'r') as rf:
        data = rf.read()
        data = nlp(data)

def unique(arg):
    all_words = sorted(set(arg))
    return all_words

def sentence_tok(arg):
    temp = [sent.text for sent in arg.sents]
    sentences= unique(temp)
    return sentences

def word_tok(arg):
    temp = [token.text for token in arg]
    words = unique(temp)
    return words

if __name__ == "__main__":
    # print(sentence_tok(data))
    print(word_tok(data))