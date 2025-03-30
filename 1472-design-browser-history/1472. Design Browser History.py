class PageNode:
    # node that holds information for our page
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = None

class BrowserHistory:
    
    def __init__(self, homepage: str):
        # initially set our current page to homepage
        self.current = PageNode(homepage)

        # S O(m) m being avg length of all page strings
        # S O(1) just assigning pointers

    def visit(self, url: str) -> None:
        # create new page with url
        # assign the current.next page to new page
        # set new page prev to current
        # set the current page to new page
        new_page = PageNode(url, self.current, None)
        self.current.next = new_page
        self.current = new_page

        # S O(m*n) n nodes every call with m avg str lengths
        # T O(1) we only reassign pointer values

    def back(self, steps: int) -> str:
        # decrement x steps from current page
        # check if current.prev exists to get to our boundary
        # return url val
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val
        
        # S O(1) no new data structures used
        # T O(min(n, steps)) either go back x steps or n available steps
        
    def forward(self, steps: int) -> str:
        # increment x steps from current page
        # check if current.next exists to get to our boundary
        # return url val
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val

        # S O(1) no new data structures used
        # T O(min(n, steps)) either go forward x steps or n available steps

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)