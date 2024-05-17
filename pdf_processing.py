import spacy
from spacypdfreader.spacypdfreader import pdf_reader
from itertools import groupby
from text_processing_methods import preprocess_text, generate_index
# from spell_checker import check_spelling

nlp = spacy.load('ru_core_news_lg')
doc = pdf_reader('met_recommendations-1-15.pdf', nlp)


cleaned_text = preprocess_text(doc)

word_usage = [[key, len(list(group))] for key, group in groupby(sorted(cleaned_text))]

sorted_word_usage = sorted(word_usage,  reverse=True, key=lambda x: x[1])

main_words_usage = sorted_word_usage[0:100]

main_words = [i[0] for i in main_words_usage] 

# print(doc[2])
# print(ord('\n'))
x = generate_index(doc, main_words)
print(x)
print(main_words_usage)
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