# pip install googletrans #to install googletranslate
##pip install googletrans==4.0.0-rc1  (solved)
  
  
"""Check supported languages"""
import googletrans

l = googletrans.LANGUAGES
for i in l:
    print(f'{i} => {l[i]}')


  
  
"""Detecting Language"""
from googletrans import Translator

translator = Translator()
text = "This is an apple"
detection = translator.detect(text)

print(f"Language: {detection.lang}, Confidence: {detection.confidence}")


  
  
"""Example 1 (default parameters)"""
from googletrans import Translator
gt = Translator()
t = gt.translate('This is a mango')
print(f'Source => {t.src}')
print(f'Destination => {t.dest}')
print(f'{t.origin} => {t.text}')


  
  
"""Example 2 (specified all parameters)"""
from googletrans import Translator

t = Translator()
gt = t.translate("What is your name?", src='en', dest='hi')
data = gt.text
print(data)



  
"""Example 3 (change destination language"""
from googletrans import Translator

t = Translator()
gt = t.translate("What is your name?",dest='hi')
print(f'Source => {gt.src}')
print(f'Destination => {gt.dest}')
print(f'{gt.origin} => {gt.text}')





  
"""Example 4 (change source language)"""
from googletrans import Translator

t = Translator()
gt = t.translate('आपका क्या नाम है?', src='hi')
data = gt.text
print(data)




"""Example 5 (auto detect source language)"""
from googletrans import Translator

t = Translator()
gt = t.translate('आपका क्या नाम है?')
data = gt.text
print(data)



"""Final code example with function"""
from googletrans import Translator

def hin2eng(query):
    gt = Translator()
    t = gt.translate(query)
    return t.text

def eng2hin(query):
    gt = Translator()
    t = gt.translate(query, dest="hi")
    return t.text



if __name__ == "__main__":
    s1 = "मेरा नाम एलेक्सा है"
    s2 = "hello there"

    eng = hin2eng(s1)
    hin = eng2hin(s2)

    print(eng)
    print(hin)