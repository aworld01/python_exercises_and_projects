##pip install googletrans #to install googletrans
##pip install googletrans==4.0.0-rc1  (solved)
  
  
##To check supported languages
# import googletrans

# l=googletrans.LANGUAGES
# for i in l:
#   print(f'{i} - {l[i]}')

query = "मेरा नाम एलेक्सा है"
query2 = "how are you"
  
  
"""Example-1 (auto detect)"""
# from googletrans import Translator

# gt=Translator()
# t=gt.translate(query)
# print(f'Source: {t.src}')
# print(f'Destination:  {t.dest}')
# print(f'{t.origin} -> {t.text}')
  
  
"""Example-2"""
# from googletrans import Translator

# gt=Translator()
# t=gt.translate(query2, src='en', dest='hi')
# print(f'Source: {t.src}')
# print(f'Destination:  {t.dest}')
# print(f'{t.origin} -> {t.text}')
  
  
"""Example-3"""
# from googletrans import Translator

# gt=Translator()
# t=gt.translate(query)
# data=t.text
# print(data)

  
"""Example-4"""
# from googletrans import Translator

# gt=Translator()
# t=gt.translate(query2, src='en', dest='hi')
# data=t.text
# print(data)

  
"""final"""
hin = "मेरा नाम एलेक्सा है"
eng = "How are you"
from googletrans import Translator

def english(query):
    gt=Translator()
    t=gt.translate(query)
    data=t.text
    return data

def hindi(query):
    gt=Translator()
    t=gt.translate(query, src="en", dest="hi")
    data=t.text
    return data

if __name__ == "__main__":
    eng = english(hin)
    hin = hindi(eng)

    print(eng)
    print(hin)