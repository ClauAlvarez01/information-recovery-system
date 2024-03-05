class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.documents = set()


class Trie:
    def __init__(self, docs_per_token):
        self.root = TrieNode()
        self.docs_per_token = docs_per_token
        self.build_trie()

    def build_trie(self):
        for word, elements in self.docs_per_token.items():
            self.insert(word, elements)

    def insert(self, word, elements):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
        node.documents = elements
    
    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return (False, set())

        return (node.end, node.documents)
