class Node:
    def __init__(self):
        self.children = {}
        self.end = False 

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = Node()

            cur = cur.children[letter]
        
        cur.end = True
        
    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            cur = root
            for i in range(j, len(word)):
                letter = word[i]
                if letter == ".":
                    for node in cur.children.values():
                        if dfs(i+1,node) == True:
                            return True
                    return False
                else:
                    if letter not in cur.children:
                        return False
                    cur = cur.children[letter]
                
            return cur.end
        return dfs(0,self.root)
