class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                charNode = TrieNode()
                node.children[ch] = charNode
            node = node.children[ch]            
        node.endWord = True

    def recSearch(self, i, word, node) -> bool:
        for j in range(i, len(word)):
            if word[j] in node.children:
                node = node.children[word[j]]
            elif word[j] == '.':
                return any([self.recSearch(j + 1, word, child) for child in node.children.values()])
            else:
                return False
        return node.endWord

    def search(self, word: str) -> bool:
        return self.recSearch(0, word, self.root)
