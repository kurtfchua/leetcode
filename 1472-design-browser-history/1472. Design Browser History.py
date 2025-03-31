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
class BrowserHistory:

    def __init__(self, homepage: str):
        

    def visit(self, url: str) -> None:
        

    def back(self, steps: int) -> str:
        

    def forward(self, steps: int) -> str:
"""
# Stack
class BrowserHistory:
    

    def __init__(self, homepage: str):
        # back stack will hold the current page and all the urls before the current page
        # front stack will hold all the urls after the current page
        self.back_history = [homepage]
        self.forward_history = []

        # S O(m) where m is the average length of all urls
        # T O(1) only assigning values
        
    def visit(self, url: str) -> None:
        # append new url to back
        # clear front history
        self.back_history.append(url)
        self.forward_history = []
        
        # S O(m*n) where m is the average length of urls and n is the amount of visits
        # T O(1) list append and assigning values are constant time

    def back(self, steps: int) -> str:
        # pop values from back history and append into front history
        # last value in front history should contain the most updated current val

        # while back history has at least one value left we pop until available steps
        while len(self.back_history) > 1 and steps > 0:
            self.forward_history.append(self.back_history.pop())
            steps -= 1
        
        return self.back_history[-1]

        # S O(1) no new data structures are being used
        # T O(min(n, steps)) the smaller of steps and actual n steps back taken

    def forward(self, steps: int) -> str:
        # pop values from front history and append into back history
        # last popped value from front will be the most current page

        # while front history has at least one value we move forward available steps
        while len(self.forward_history) > 0 and steps > 0:
            self.back_history.append(self.forward_history.pop())
            steps -= 1
        
        return self.back_history[-1]

        # S O(1) no new data structures are used
        # T O(min(n, steps)) the smaller between steps and actual n steps forward taken



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)