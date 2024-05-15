import spacy
from spacypdfreader.spacypdfreader import pdf_reader
from itertools import groupby

nlp = spacy.load('ru_core_news_lg')
doc = pdf_reader('met_recommendations-1-10.pdf', nlp)


def preprocess_text(doc):
    cleaned_tokens = []
    for token in doc:
        if not token.is_space and not token.is_punct and not token.like_num and not token.is_title:
            cleaned_tokens.append(token.lemma_.lower())
        # if token.is_title:
        #     cleaned_tokens.append(token.text)
    return cleaned_tokens

def generate_index(doc, words_list):
    index = {}
    line_number = 0
    page_number = 1

    for i in range(len(doc)):
        word_from_original = str(doc[i].lemma_.lower())
        if word_from_original in words_list and word_from_original not in index:
            index[word_from_original] = {'номер страницы: ': page_number, 'номер строки: ': line_number}
        
        if '\n' in str(doc[i]):
            line_number += 1

        if page_number != doc[i]._.page_number:
            line_number = 1
            page_number = doc[i]._.page_number

    return index


cleaned_text = preprocess_text(doc)

word_usage = [[key, len(list(group))] for key, group in groupby(sorted(cleaned_text))]
sorted_word_usage = sorted(word_usage,  reverse=True, key=lambda x: x[1]) 

main_words_usage = sorted_word_usage[0:100]

main_words = [i[0] for i in main_words_usage] 

# print(doc[2])
# print(ord('\n'))
print(generate_index(doc, main_words))
# print(doc._.page(1))








# Get the page number of any token.
# print(doc[0]._.page_number)  # 1
# print(doc[-1]._.page_number) # 4

# print(doc._.page_range)      # (1, 4)
# print(doc._.first_page)      # 1
# print(doc._.last_page)       # 4
# print(str(doc._.page(10)))
# Get all of the text from a specific PDF page.
# print(doc._.page(3))         # able to display the destination page