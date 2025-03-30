class PageNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = PageNode(homepage)

    def visit(self, url: str) -> None:
        # set last node next to new visited node
        # set visited node prev to current node
        # set current node to visited node
        self.current.next = PageNode(url, None, self.current)
        self.current = self.current.next
         
    def back(self, steps: int) -> str:
        # decrement back to amount of steps to current node
        # check if current.prev exists and if steps > 0 in loop
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1

        return self.current.val
        
    def forward(self, steps: int) -> str:
        # increment forward amount of steps to current node
        # check if current.next exists and if steps > 0 in loop
        while self.current.next and steps > 0 :
            self.current = self.current.next
            steps -=1 
        
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)