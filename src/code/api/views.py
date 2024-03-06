import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from api.trie import Trie
from api.boolean_model import BooleanModel
from api.LSI_model import lsi_model
from api.evaluations import Evaluation
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words_english = set(stopwords.words('english'))


documents = {}
vocabulary = {}
queries = {}
trecQrel = {}
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

queries_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', '..', '..', 'data', 'querys.json')
queries_path = os.path.abspath(queries_path)

trecQrel_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', '..', '..', 'data', 'trecQrel.json')
trecQrel_path = os.path.abspath(trecQrel_path)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~ Load jsons ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open(docs_per_token_path, 'r') as docs_per_token_file:
    docs_per_token = json.load(docs_per_token_file)
docs_per_token_values = docs_per_token['docs_per_token']

with open(documents_path, 'r') as documents_file:
    documents = json.load(documents_file)
documents_values = list(documents['documents'].values())

with open(vocabulary_path, 'r') as vocabulary_file:
    vocabulary = json.load(vocabulary_file)
vocabulary_values = vocabulary['vocabulary']

with open(cranfield_docs_path, 'r') as cranfield_docs_file:
    cranfield_docs = json.load(cranfield_docs_file)

with open(queries_path, 'r') as queries_file:
    queries = json.load(queries_file)
queries_values = queries['querys']

with open(trecQrel_path, 'r') as trecQrel_file:
    trecQrel = json.load(trecQrel_file)
trecQrel_values = trecQrel['trecQrel']
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Models ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nlp = spacy.load("en_core_web_sm")

trie = Trie(docs_per_token_values)
boolean_model = BooleanModel(nlp, trie)


vectorizer = TfidfVectorizer(vocabulary=vocabulary_values)
matrix, lsa_model = lsi_model(documents_values, vectorizer)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# http://localhost:8000/api/queries
@api_view(['GET'])
def queries(request):
    data = []

    print(len(queries_values.items()))
    for query_id, text_list in queries_values.items():
        text = text_list[0]
        data.append({
            "query_id": query_id,
            "text": text
        })

    return Response({'data': data})


# http://localhost:8000/api/test
@api_view(['GET'])
def test(request):
    docs = [
        {
            'doc_id': '1',
            'title': 'Título del Documento 1',
            'text': 'Texto del Documento 1. Este es un ejemplo de un texto más extenso para el Documento 1. Puede contener información detallada y relevante.',
            'author': 'Autor 1',
            'bib': 'Bibliografía 1'
        },
        {
            'doc_id': '2',
            'title': 'Título del Documento 2',
            'text': 'Texto del Documento 2. Aquí hay más contenido para el Documento 2. Puede incluir detalles, ejemplos y cualquier información adicional que sea necesaria.',
            'author': 'Autor 2',
            'bib': 'Bibliografía 2'
        },
        {
            'doc_id': '3',
            'title': 'Título del Documento 3',
            'text': 'Texto del Documento 3. Este documento tiene un texto más extenso que aborda varios temas importantes. Puede contener secciones y subsecciones.',
            'author': 'Autor 3',
            'bib': 'Bibliografía 3'
        },
        {
            'doc_id': '4',
            'title': 'Título del Documento 4',
            'text': 'Texto del Documento 4. En este documento, se discuten diversas ideas y conceptos. Se proporcionan ejemplos y análisis detallados.',
            'author': 'Autor 4',
            'bib': 'Bibliografía 4'
        },
        {
            'doc_id': '5',
            'title': 'Título del Documento 5',
            'text': 'Texto del Documento 5. Aquí encontrarás una amplia gama de información relacionada con el tema principal. El autor ofrece insights y conclusiones.',
            'author': 'Autor 5',
            'bib': 'Bibliografía 5'
        },
        {
            'doc_id': '6',
            'title': 'Título del Documento 6',
            'text': 'Texto del Documento 6. Este documento explora aspectos específicos y proporciona datos detallados. Puede ser de interés para expertos en el campo.',
            'author': 'Autor 6',
            'bib': 'Bibliografía 6'
        },
        {
            'doc_id': '7',
            'title': 'Título del Documento 7',
            'text': 'Texto del Documento 7. Aquí se presentan casos de estudio y ejemplos prácticos. El autor analiza y extrae lecciones valiosas de cada situación.',
            'author': 'Autor 7',
            'bib': 'Bibliografía 7'
        },
        {
            'doc_id': '8',
            'title': 'Título del Documento 8',
            'text': 'Texto del Documento 8. Este documento se centra en investigaciones recientes y descubrimientos. Proporciona una visión actualizada del estado del campo.',
            'author': 'Autor 8',
            'bib': 'Bibliografía 8'
        },
        {
            'doc_id': '9',
            'title': 'Título del Documento 9',
            'text': 'Texto del Documento 9. Aquí se abordan controversias y debates en el campo. El autor presenta diferentes perspectivas y argumentos.',
            'author': 'Autor 9',
            'bib': 'Bibliografía 9'
        },
        {
            'doc_id': '10',
            'title': 'Título del Documento 10',
            'text': 'Texto del Documento 10. Este documento sirve como una revisión exhaustiva de la literatura existente. El autor destaca tendencias y brechas en la investigación.',
            'author': 'Autor 10',
            'bib': 'Bibliografía 10'
        }
    ]
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
        },
        'fallout': {
            'boolean': '0.31',
            'other': '0.41'
        }
    }

    return Response({'docs': docs, 'metrics': metrics})


@api_view(['GET'])
def search(request):
    query = request.GET.get('query', '')
    id = request.GET.get('id', '-1')
    query = query.lower()

    query_vector = vectorizer.transform([query])
    semantic_query = lsa_model.transform(query_vector)

    similarity = cosine_similarity(semantic_query, matrix)
    similar_indexes = similarity.argsort()[0][-10:][::-1]
    similar_indexes = [i+1 for i in similar_indexes]

    docs = []
    cranfield_docs_values = cranfield_docs['cranfieldDoc']

    for i in similar_indexes:
        docs.append(cranfield_docs_values[str(i)])

    if id != '-1' and id in trecQrel_values:
        positive_similarity_indexes = [
            i+1 for i, sim in enumerate(similarity[0]) if sim > 0]
        recovered_docs = []
        for i in positive_similarity_indexes:
            recovered_docs.append(cranfield_docs_values[str(i)]['doc_id'])

        evaluation_lsi_model = Evaluation(trecQrel_values[id], recovered_docs)
        lsi_precision, lsi_recall, lsi_f1, lsi_fallout = evaluation_lsi_model.apply_metrics()
        if lsi_precision == -1:
            lsi_precision = "NaN"
        if lsi_recall == -1:
            lsi_recall = "NaN"
        if lsi_f1 == -1:
            lsi_f1 = "NaN"
        if lsi_fallout == -1:
            lsi_fallout = "NaN"

        split_query = query.split()

        logical_query = ""
        first = True
        for item in split_query:
            word = nlp(item)
            if item not in stop_words_english and item.isalpha():
                if first:
                    logical_query += word[0].lemma_
                    first = False
                else:
                    logical_query += ' AND ' + word[0].lemma_

        docs_output_query_dnf = boolean_model.get_matching_docs(logical_query)

        if len(docs_output_query_dnf) != 0:
            evaluation_boolean_model = Evaluation(
                trecQrel_values[id], docs_output_query_dnf)
            boolean_precision, boolean_recall, boolean_f1, boolean_fallout = evaluation_boolean_model.apply_metrics()
        else:
            boolean_precision, boolean_recall, boolean_f1, boolean_fallout = "NaN", "NaN", "NaN", "NaN"
        
        metrics = {
            'precision': {
                'boolean': boolean_precision,
                'lsi': lsi_precision
            },
            'recovered': {
                'boolean': boolean_recall,
                'lsi': lsi_recall
            },
            'f1': {
                'boolean': boolean_f1,
                'lsi': lsi_f1
            },
            'fallout': {
                'boolean': boolean_fallout,
                'lsi': lsi_fallout
            }
        }
    else:
        metrics = {}

    return Response({'docs': docs, 'metrics': metrics})
