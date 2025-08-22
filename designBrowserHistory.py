class DLN:
    def __init__(self, val):
        self.val,self.nxt,self.prev = val,None,None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DLN(homepage)
        
    def visit(self, url: str) -> None:
        new_node = DLN(url)
        new_node.prev = self.history
        self.history.nxt = new_node
        self.history = self.history.nxt

    def back(self, steps: int) -> str:
        while steps and self.history.prev:
            self.history = self.history.prev
            steps -= 1
        return self.history.val
    
    def forward(self, steps: int) -> str:
        while steps and self.history.nxt:
            self.history = self.history.nxt
            steps -= 1
        return self.history.val
