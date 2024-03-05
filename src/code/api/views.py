import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from api.trie import Trie
from api.boolean_model import BooleanModel
from api.LSI_model import lsi_model
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


documents = {}
vocabulary = {}
cranfield_docs = {}
docs_per_token = {}


# ~~~~~~~~~~~~~~~~~~~~~~~~ Data paths ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
docs_per_token_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', '..', '..', 'data', 'docs_per_token.json')
docs_per_token_path = os.path.abspath(docs_per_token_path)

documents_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', '..', '..', 'data', 'documents.json')
documents_path = os.path.abspath(documents_path)

vocabulary_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', '..', '..', 'data', 'vocabulary.json')
vocabulary_path = os.path.abspath(vocabulary_path)

cranfield_docs_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', '..', '..', 'data', 'cranfieldDoc.json')
cranfield_docs_path = os.path.abspath(cranfield_docs_path)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~ Load jsons ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open(docs_per_token_path, 'r') as docs_per_token_file:
    docs_per_token = json.load(docs_per_token_file)

with open(documents_path, 'r') as documents_file:
    documents = json.load(documents_file)
documents_values = list(documents['documents'].values())

with open(vocabulary_path, 'r') as vocabulary_file:
    vocabulary = json.load(vocabulary_file)
vocabulary_values = vocabulary['vocabulary']

with open(cranfield_docs_path, 'r') as cranfield_docs_file:
    cranfield_docs = json.load(cranfield_docs_file)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Models ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nlp = spacy.load("en_core_web_sm")

trie = Trie(docs_per_token['docs_per_token'])
boolean_model = BooleanModel(nlp, trie)


vectorizer = TfidfVectorizer(vocabulary=vocabulary_values)
matrix, lsa_model = lsi_model(documents_values, vectorizer)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# http://localhost:8000/api/test
@api_view(['GET'])
def test(request):
    return Response({'message': 'Hello, world!'})


@api_view(['GET'])
def search(request):
    query = "material properties of photoelastic materials ."

    query_vector = vectorizer.transform([query])
    semantic_query = lsa_model.transform(query_vector)

    similarity = cosine_similarity(semantic_query, matrix)
    similar_indexes = similarity.argsort()[0][-10:][::-1]
    similar_indexes = [i+1 for i in similar_indexes]

    docs = []
    cranfield_docs_values = list(cranfield_docs['cranfieldDoc'].values())

    for i in similar_indexes:
        docs.append(cranfield_docs_values[i])

    metrics = {
        'precision': {
            'boolean': '0.57',
            'other': '0.90'
        },
        'recovered': {
            'boolean': '0.20',
            'other': '0.46'
        },
        'f1': {
            'boolean': '0.39',
            'other': '0.49'
        }
    }
    return Response({'docs': docs, 'metrics': metrics})
