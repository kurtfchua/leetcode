"""
class BrowserHistory:

    def __init__(self, homepage: str):
        

    def visit(self, url: str) -> None:
        

    def back(self, steps: int) -> str:
        

    def forward(self, steps: int) -> str:
class BrowserHistory:

    def __init__(self, homepage: str):
        

    def visit(self, url: str) -> None:
        

    def back(self, steps: int) -> str:
        

    def forward(self, steps: int) -> str:
"""

# Linked List
class PageNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class BrowserHistory:

    def __init__(self, homepage: str):
        # init homepage to current value
        self.current = PageNode(homepage)
        
        # S O(m) where m is the average of all the page names in the list
        # T O(1) only assigning values

    def visit(self, url: str) -> None:
        # create new page node with url name
        # assign self.current -> <-page node
        # assign self.current to the new node
        new_node = PageNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node
        
        # S O(m*n) where m is the size of the str and n is the amount of visit calls
        # T O(1) just assigning values

    def back(self, steps: int) -> str:
        # while current.prev exists iterate until we reach available steps
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1

        return self.current.val

        # S O(1) we don't create new data strutures
        # T O(min(steps, n)) where n is the actual amount of possible shifting
        
    def forward(self, steps: int) -> str:
        # while current.next exists iterate until we reach available steps
        while self.current.next and steps:
            self.current = self.current.next 
            steps -= 1
        
        return self.current.val

        # S O(1) we don't create new data structures
        # T O(min(steps, n)) where n is the actual amount of possible shifting

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)