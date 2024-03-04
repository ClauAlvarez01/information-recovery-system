from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
            'vectorial': '0.90'
        },
        'recovered': {
            'boolean': '0.20',
            'vectorial': '0.46'
        },
        'f1': {
            'boolean': '0.39',
            'vectorial': '0.49'
        }
    }

    return Response({'docs': docs, 'metrics': metrics})