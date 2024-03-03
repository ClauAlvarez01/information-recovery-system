class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.documents = set()


class Trie:
    def __init__(self, tokenized_docs):
        self.root = TrieNode()
        self.tokenized_docs = tokenized_docs

    def build_trie(self, words):
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
        node.documents = self.get_docs_for_token(word)

    def get_docs_for_token(self, token):
        documents = set()
        for i, doc in enumerate(self.tokenized_docs):
            if token in doc:
                documents.add(i+1)
        return documents
    
    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return (False, set())

        return (node.end, node.documents)
