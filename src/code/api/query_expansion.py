import nltk
nltk.download('wordnet')
from nltk.wsd import lesk

def get_synsets_for_context(tokenized_query):
    """
    Get correct definition for each word in query for the given context

    Args:
        - query (list<str>) : Tokenized query

    Return:
        list<Synset>

    """
    synsets = [lesk(tokenized_query, word) for word in tokenized_query]
    return synsets


def expand_with_wordnet(tokenized_query):
    """
    Expand the query using synonyms

    Args:
        - query (list<str>) : Tokenized query

    Return:
        list<str>

    """

    if len(tokenized_query) >= 5:
        return ' '.join(tokenized_query)
    
    synsets = get_synsets_for_context(tokenized_query)
    expanded_query = []

    for synset in synsets:
        if synset:
            # Obtener sinónimos del synset
            synonyms = [lemma for lemma in synset.lemma_names()]
            # Agregar los sinónimos a la lista expandida
            expanded_query.extend(synonyms)

    return expanded_query


