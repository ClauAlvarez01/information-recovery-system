import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.wsd import lesk


def get_query_expand(query):
    """
    Expand a query using synonyms found in WordNet, a lexical database of English that contains semantic relationships between words. 
    If the query has 5 or more words, the original query is returned unchanged. 
    Otherwise, synonyms are searched for each word in the query, taking into account the context of the query, and the query is expanded by including these synonyms.

    Parameters:
    - query (str): The query to expand.

    Returns:
    - str: The original query or an expanded version with synonyms found in WordNet based on the context of the query.
    """

    words = query.split()

    if len(words) >= 5:
        return query
    
    synonyms = get_synonyms(query)

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


def get_synonyms(query):
    """
    Retrieve synonyms for each word in the given query using WordNet, considering the context of the query.
    
    Parameters:
    - query (str): The input query to find synonyms for.

    Returns:
    - dict: A dictionary containing words from the query as keys and lists of their synonyms as values.
    """

    words = query.split()

    disambiguated_synsets = [lesk(words, word) for word in words]
    
    synonyms_per_word = {}

    for word, disambiguated_synsets in zip(words, disambiguated_synsets):
        word_synsets = wordnet.synsets(word)

        if not word_synsets:
            continue
        
        highest_similarity = 0.0
        synonyms = []

        for word_synset in word_synsets:
            similarity = disambiguated_synsets.wup_similarity(word_synset)

            if similarity is not None and similarity >= highest_similarity:
                # most_similar_synset = word_synset
                highest_similarity = similarity

                synonyms.append(
                    [lemma.name() for lemma in word_synset.lemmas() if lemma.name() != word])

        result = list(set(item for array in synonyms for item in array))

        if word in synonyms_per_word:
            synonyms_per_word[word].extend(set(result))
        else:
            synonyms_per_word[word] = list(set(result))

    return synonyms_per_word 
