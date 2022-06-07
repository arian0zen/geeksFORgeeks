#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None


class Solution:
     def sortedListToBST(self, head):
        if head is None:
            return None
        if head.next is None:
            return TNode(head.data)
        fast = head
        slow = head
        prev = LNode(None)
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        mid = slow
        root = TNode(mid.data)
        prev.next=None
        root.left = self.sortedListToBST(head)
        if mid.next:
            root.right = self.sortedListToBST(mid.next)
        return root