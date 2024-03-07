import re
from sympy import And, symbols, sympify, to_dnf
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words_english = set(stopwords.words('english'))


class BooleanModel:
    def __init__(self, nlp, trie):
        self.nlp = nlp
        self.trie = trie

    def query_to_dnf(self, query):
        """
        Returns the converted and simplified logical expression to its disjunctive normal form.

        Arg:
            - query (str): Input query.

        Return:
            query_dnf(str): Query expressed in normal disjunctive form.
        """
        tokens = [token.lemma_.lower() for token in self.nlp(query) if (token.text.lower() not in stop_words_english and token.is_alpha) or token.text == ")" or token.text == "("]

        # processed_query = ' '.join(tokens).replace("and", "&").replace("or", "|").replace("not", "~")

        try:
            processed_query = ' & ' .join(tokens)
            query_expr = sympify(processed_query, evaluate=False)
        except:
            processed_query = ' ' .join(tokens)
            elements = symbols(processed_query)
            query_expr = And(*elements)
            query_expr = sympify(query_expr, evaluate=False)

        query_dnf = to_dnf(query_expr, force=True)

        return query_dnf

    def get_matching_docs(self, query_dnf):
        """
        Retrieves documents that match the given Disjunctive Normal Form (DNF) query.

        Args:
            - query_dnf (str): Disjunctive Normal Form (DNF) query.

        Returns:
            list: List of documents that satisfy the given DNF query.
        """
        conjunctive_clauses = re.findall(r'\((.*?)\)|(\w+)|(\w+\s*\|\s*\w+)', str(query_dnf)) 
        conjunctive_clauses = [ 
            re.split(r'\s*&\s*', clause[0]) if clause[0] else 
            re.split(r'\s*\|\s*', clause[2]) if clause[2] else 
            [clause[1]] 
            for clause in conjunctive_clauses 
        ]

        matching_documents = []

        for clause in conjunctive_clauses:
            matching_documents.append(self.get_documents(clause))

        intersection_matching_docs = set(matching_documents[0]).intersection(*matching_documents[1:])
        return (list(intersection_matching_docs))

    def get_documents(self, clause):
        """
        Retrieves documents based on a given clause.

        Args:
            - clause (list): List of elements representing a logical clause.

        Returns:
            list: List of documents that satisfy the given logical clause.
        """
        all_docs = []
        set_docs = set(str(range(1, 1401)))
        for element in clause:
            if element.startswith("~"):
                (end, docs) = self.trie.search(element[1:])
                if end:
                    difference_set = set_docs.difference(docs)
                    all_docs.append(list(difference_set))
                else:
                    return set()
            else:
                all_docs.append(list(self.trie.search(element)[1]))

        interseccion_docs = set.intersection(*map(set, all_docs))
        return (list(interseccion_docs))

    