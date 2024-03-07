import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet


def get_query_expand(query):
    """
    Expand a query using synonyms found in WordNet, a lexical database of English that contains semantic relationships between words. If the query has 5 or more words, the original query is returned unchanged. Otherwise, synonyms are searched for each word in the query, and the query is expanded by including these synonyms.

    Parameters:
    - query (str): The query to expand.

    Returns:
    - str: The original query or an expanded version with synonyms found in WordNet.

    """
    words = query.split()
    if len(words) >= 5:
        return query
    
    synonyms = {}
    for word in words:
        try:
            word_synset = wordnet.synsets(word)[0]
            similar_synsets = [synset for synset in wordnet.synsets(word) if synset != word_synset]
            sorted_synsets = sorted(similar_synsets, key=lambda x: word_synset.wup_similarity(x), reverse=True)
            top_synsets = sorted_synsets[:2] if sorted_synsets else []
            synonyms[word] = [lemma.name() for synset in top_synsets for lemma in synset.lemmas()[:2]]
        except IndexError:
            continue
    
    parts_of_query_extension = []
    
    for word in words:
        if word in synonyms:
            synonym_list = [synonym for synonym in synonyms[word] if synonym not in words]
            if synonym_list:
                parts_of_query_extension.append(f"{word} {' '.join(synonym_list)}")
            else:
                parts_of_query_extension.append(word)
        else:
            parts_of_query_extension.append(word)

    query_expand = ' '.join(parts_of_query_extension)

    return query_expand
