from sklearn.decomposition import TruncatedSVD

def lsi_model(documents, vectorizer):

    tfidf_matrix = vectorizer.fit_transform(documents)
    lsa_model = TruncatedSVD(n_components=100)
    lsa_topic_matrix = lsa_model.fit_transform(tfidf_matrix)
    return lsa_topic_matrix, lsa_model