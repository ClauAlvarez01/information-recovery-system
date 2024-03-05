class Metrics:
    def __init__(self, relevant_recovered, irrelevant_recovered, relevant_not_recovered, irrelevant_docs):
        self.precision_value = self.precision(relevant_recovered, irrelevant_recovered)
        self.recall_value = self.recall(relevant_recovered, relevant_not_recovered)
        self.f1_value = self.f1()
        self.fallout_value = self.fallout(irrelevant_recovered, irrelevant_docs)

    def precision(self, relevant_recovered, irrelevant_recovered):
        return len(relevant_recovered)/ len(set(relevant_recovered).union(set(irrelevant_recovered)))

    def recall(self, relevant_recovered, relevant_not_recovered):
        return len(relevant_recovered)/ len(set(relevant_recovered).union(set(relevant_not_recovered)))
    
    def f1(self):
        return ((2*self.precision_value*self.recall_value)/ (self.precision_value+self.recall_value))
    
    def fallout(self, irrelevant_recovered, irrelevant_docs):
        return len(irrelevant_recovered)/ len(irrelevant_docs) 
