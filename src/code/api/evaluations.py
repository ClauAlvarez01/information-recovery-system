from api.metrics import Metrics

class Evaluation():
    def __init__(self, trecQrel ,recovered_documents):
        self.trecQrel = trecQrel
        self.recoveredDocs = recovered_documents
        self.relevant_docs = []
        self.irrelevant_docs = []
        self.relevant_recovered = []
        self.relevant_not_recovered = []
        self.irrelevant_recovered = []

        for element in trecQrel.items():
            if element['relevance'] >= 3:
                self.relevant_docs.append(element['doc_id'])
            else:
                self.irrelevant_docs.append(element['doc_id'])
    
        self.relevant_recovered = set(self.relevant_docs).intersection(set(self.recoveredDocs))
        self.relevant_not_recovered = set(self.relevant_docs).difference(set(self.relevant_recovered))
        self.irrelevant_recovered = set(self.irrelevant_docs).intersection(set(self.recoveredDocs))

    def apply_metrics(self):
        metrics_values = Metrics(self.relevant_recovered, self.irrelevant_recovered, self.relevant_not_recovered, self.irrelevant_docs)

        return metrics_values.precision_value, metrics_values.recall_value, metrics_values.f1_value, metrics_values.fallout_value

    