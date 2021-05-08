class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def solve(self, head):
        if head.next==None:
            return True
        while head.next:
            if head.next.val<=head.val:
                return False
            head=head.next
        return True