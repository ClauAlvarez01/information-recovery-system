import re
from sympy import sympify, to_dnf

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
        tokens = [token.lemma_.lower() for token in self.nlp(query) if token.is_alpha or token.text == ")" or token.text == "("]

        processed_query = ' '.join(tokens).replace("and", "&").replace("or", "|").replace("not", "~")

        query_expr = sympify(processed_query, evaluate=False)
        query_dnf = to_dnf(query_expr, simplify=True)

        return query_dnf

    def get_matching_docs(self, query_dnf):
        """
        Retrieves documents that match the given Disjunctive Normal Form (DNF) query.

        Args:
            - query_dnf (str): Disjunctive Normal Form (DNF) query.

        Returns:
            list: List of documents that satisfy the given DNF query.
        """
        conjunctive_clauses = re.findall(r'\((.*?)\)|(\w+)', query_dnf)
        conjunctive_clauses = [re.split(
            r'\s*&\s*', clause[0]) if clause[0] else [clause[1]] for clause in conjunctive_clauses]

        matching_documents = []

        for clause in conjunctive_clauses:
            matching_documents.append(self.get_documents(clause))

        union_matching_docs = set().union(*matching_documents)
        return (list(union_matching_docs))

    def get_documents(self, clause):
        """
        Retrieves documents based on a given clause.

        Args:
            - clause (list): List of elements representing a logical clause.

        Returns:
            list: List of documents that satisfy the given logical clause.
        """
        all_docs = []
        for element in clause:
            if element.startswith("~"):
                (end, docs) = self.trie.search(element[1:])
                if end:
                    set_docs = set(str(range(1, 1401)))
                    difference_set = set_docs.difference(docs)
                    all_docs.append(list(difference_set))
                else:
                    return set()
            else:
                all_docs.append(list(self.trie.search(element)[1]))

        interseccion_docs = set.intersection(*map(set, all_docs))
        return (list(interseccion_docs))

    