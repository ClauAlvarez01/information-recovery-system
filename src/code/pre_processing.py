import spacy
import gensim
import sys
import os
import ir_datasets
ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(ruta_src)

def load_corpus():
    dataset = ir_datasets.load("cranfield")
    # documents = [doc.text for doc in dataset.docs_iter()]
    cranfieldDoc = {}
    documents = []
    for doc in dataset.docs_iter():
        cranfieldDoc[doc[0]] = {'doc_id': doc[0], 
                                    'title': doc[1],
                                    'text': doc[2],
                                    'author': doc[3],
                                    'bib': doc[4]}
        documents.append(doc.text)

    genericQuery = {}
    for query in dataset.queries_iter():
        genericQuery[query[0]] = [query[1]]
    
    trecQrel = {}
    for qrel in dataset.qrels_iter():
        trecQrel[qrel[0]] = {'doc_id': qrel[1],
                             'relevance': qrel[2], 
                             'iteration': qrel[3]}

    return cranfieldDoc, documents, genericQuery, trecQrel

class ProcessingData:

    def __init__(self, nlp):
        self.nlp = nlp
        self.cranfieldDoc, self.documents, self.querys, self.trecQrel  = load_corpus()
        self.tokenized_docs = self.process_documents(self.documents)
        self.dictionary = gensim.corpora.Dictionary(self.tokenized_docs)
        self.tokenized_docs = self.filter_tokens_by_occurrence(
            self.tokenized_docs, self.dictionary)
        self.vocabulary = self.build_vocabulary()
        self.vector_repr = self.vector_representation()

    def process_documents(self, documents):
        tokenized_docs = self.tokenization_spacy(documents)
        tokenized_docs = self.remove_noise_spacy(tokenized_docs)
        tokenized_docs = self.remove_stopwords_spacy(tokenized_docs)
        tokenized_docs = self.morphological_reduction_spacy(tokenized_docs)
        
        return tokenized_docs

    # Tokenización
    def tokenization_spacy(self, texts):
        return [[token for token in self.nlp(doc)] for doc in texts]

    # Eliminación de Ruido
    def remove_noise_spacy(self, tokenized_docs):
        return [[token for token in doc if token.is_alpha] for doc in tokenized_docs]

    # Eliminación de Stop-Words
    def remove_stopwords_spacy(self, tokenized_docs):
        stopwords = spacy.lang.en.stop_words.STOP_WORDS
        return [[token for token in doc if token.text.lower() not in stopwords] for doc in tokenized_docs]

    # Reducción Morfológica
    def morphological_reduction_spacy(self, tokenized_docs):
        return [[token.lemma_ for token in doc] for doc in tokenized_docs]

    # Filtrado según ocurrencia
    def filter_tokens_by_occurrence(self, tokenized_docs, dictionary, no_below=5, no_above=0.5):
        dictionary.filter_extremes(no_below=no_below, no_above=no_above)
        filtered_words = [word for _, word in dictionary.iteritems()]
        return [[word for word in doc if word in filtered_words] for doc in tokenized_docs]

    # Construcción del vocabulario
    def build_vocabulary(self):
        return list(self.dictionary.token2id.keys())

    # Representación vectorial de Docs
    def vector_representation(self):
        corpus = [self.dictionary.doc2bow(doc) for doc in self.tokenized_docs]

        tfidf = gensim.models.TfidfModel(corpus)
        vector_repr = [tfidf[doc] for doc in corpus]

        return vector_repr

    # #Etiquetado
    # def pos_tagger_spacy(self):
    #     return [[(token.text, token.tag_) for token in doc] for doc in self.tokenized_docs]
    # def pos_tagger_spacy(tokenized_docs):
    #     return [[(token.text, token.tag_) for token in doc] for doc in tokenized_docs]


