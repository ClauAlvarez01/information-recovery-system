import spacy
import sys
import os
import json
from pre_processing import ProcessingData
ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(ruta_src)

nlp_instance=spacy.load("en_core_web_sm")

processing_data = ProcessingData(nlp_instance)

cranfieldDoc = processing_data.cranfieldDoc 
documents = {i + 1: doc for i, doc in enumerate(processing_data.documents)}
querys = processing_data.querys
trecQrel = processing_data.trecQrel

documents_per_token = {}
for index, token in enumerate(processing_data.tokenized_docs):
    for item in token: 
        if item in documents_per_token:
            if not (index+1) in documents_per_token[item]:
                documents_per_token[item].append(index+1)
        else:
            documents_per_token[item] = [index+1]


def save_documents_to_json(text, json_file_name, file='data'):
        json_path = os.path.join(file, json_file_name)
        file_name = json_file_name.split('.')
        data = {file_name[0]: text}

        try:
            json_string = json.dumps(data, indent=2)
            with open(json_path, 'w', encoding='utf-8') as file_json:
                file_json.write(json_string)
                print(f"La exportación a {json_path} se realizó con éxito.")
        except Exception as e:
            print(f"Error al exportar a JSON: {e}")

save_documents_to_json(documents, 'documents.json', file='data')
save_documents_to_json(documents_per_token, 'docs_per_token.json', file='data')
save_documents_to_json(processing_data.tokenized_docs, 'tokenized_docs.json', file='data')
save_documents_to_json(cranfieldDoc, 'cranfieldDoc.json', file='data')
save_documents_to_json(querys, 'querys.json', file='data')
save_documents_to_json(trecQrel, 'trecQrel.json', file='data')
save_documents_to_json(processing_data.vocabulary, 'vocabulary.json', file='data')