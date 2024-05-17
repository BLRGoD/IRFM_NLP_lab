


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