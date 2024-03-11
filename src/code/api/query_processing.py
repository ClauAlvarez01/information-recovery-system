import spacy

def get_tokenized_query(nlp, query):
    doc = nlp(query)
    tokens = []
    for token in doc:
        tags = ['ADJ', 'NOUN', 'VERB', 'ADV']
        if token.pos_ in tags:
            tokens.append(token.lemma_)

    return tokens

