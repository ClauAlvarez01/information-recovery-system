from sklearn.decomposition import TruncatedSVD

def lsi_model(documents, vectorizer):
    """
    Applies Latent Semantic Indexing (LSI) to a collection of documents.

    Parameters:
    - documents (list): A list of strings representing the input documents.
    - vectorizer: The vectorizer object used to convert the input documents into a TF-IDF matrix.

    Returns:
    - lsa_topic_matrix (numpy.ndarray): The matrix containing the LSA topic representation of the input documents.
    - lsa_model: The TruncatedSVD model fitted on the TF-IDF matrix.
    """
    
    tfidf_matrix = vectorizer.fit_transform(documents)
    lsa_model = TruncatedSVD(n_components=100)
    lsa_topic_matrix = lsa_model.fit_transform(tfidf_matrix)
    return lsa_topic_matrix, lsa_model