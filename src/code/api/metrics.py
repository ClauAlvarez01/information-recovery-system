class Metrics:
    def __init__(self, relevant_recovered, irrelevant_recovered, relevant_not_recovered, irrelevant_docs):
        self.precision_value = self.precision(relevant_recovered, irrelevant_recovered)
        self.recall_value = self.recall(relevant_recovered, relevant_not_recovered)
        self.f1_value = self.f1()
        self.fallout_value = self.fallout(irrelevant_recovered, irrelevant_docs)

    def precision(self, relevant_recovered, irrelevant_recovered):
        print(len(relevant_recovered))
        print(len(set(relevant_recovered).union(set(irrelevant_recovered))))
        response = -1
        try:
            response = len(relevant_recovered)/ len(set(relevant_recovered).union(set(irrelevant_recovered)))
        except:
            pass
        return response 

    def recall(self, relevant_recovered, relevant_not_recovered):
        response = -1
        try:
            response = len(relevant_recovered)/ len(set(relevant_recovered).union(set(relevant_not_recovered)))
        except:
            pass
        return response
    
    def f1(self):
        response = -1
        try:
            response = ((2*self.precision_value*self.recall_value)/ (self.precision_value+self.recall_value))
        except:
            pass
        return response
    
    def fallout(self, irrelevant_recovered, irrelevant_docs):
        response = -1
        try:
            response = len(irrelevant_recovered)/ len(irrelevant_docs)
        except:
            pass
        return response
