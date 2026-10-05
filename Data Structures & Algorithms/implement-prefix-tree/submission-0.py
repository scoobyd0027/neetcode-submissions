class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.endWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                charNode = TrieNode(ch)
                node.children[ch] = charNode
            node = node.children[ch]            
        node.endWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]  
        return node.endWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch] 
        return True
