from spellchecker import SpellChecker

import spacy
from spacypdfreader.spacypdfreader import pdf_reader
from itertools import groupby

nlp = spacy.load('ru_core_news_lg')
doc = pdf_reader('test_wrong_spelling.pdf', nlp)

def check_spelling(doc, nlp):
    spell = SpellChecker(language='ru')

    corrected_tokens = []
    
    for token in doc:
        if not token.is_space and not token.is_punct and not token.like_num:
            word = token.text
            corrected_word = spell.correction(word)

            if corrected_word != word:
                word = corrected_word                
            
            corrected_tokens.append(word)
    
    corrected_tokens = [token for token in corrected_tokens if token is not None and token != '']
    corrected_doc = spacy.tokens.Doc(nlp.vocab, words=corrected_tokens)

    return corrected_doc

# print(doc)
# print(check_spelling(doc, nlp))

x = check_spelling(doc, nlp)
print(x)
# for i in range(len(doc)):
    # print(i,': ',doc[i].text)