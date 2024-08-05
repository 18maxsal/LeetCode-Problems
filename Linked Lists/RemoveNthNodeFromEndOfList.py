# Link to Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(val= 0 , next= head) # Creating a dummy node to make traversal easier without having the need 
        # for a prev node variable
        left = dummyNode
        right = head

        while n > 0 and right: # Ensuring that left and right nodes are n nodes apart 
            right = right.next
            n -= 1
        
        while right: # Iterating until right is Null
            left = left.next
            right = right.next
        
        left.next = left.next.next # Removing nth node

        return dummyNode.next # Returning the head of the list

# node1 = ListNode(val=1, next= None)
# node2 = ListNode(val=2, next= None)
# node3 = ListNode(val=3, next= None)
# node4 = ListNode(val=4, next= None)
# node5 = ListNode(val=5, next=None)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

node1 = ListNode(val=1, next= None)
node2 = ListNode(val=2, next= None)

node1.next = node2

test = Solution()
result = test.removeNthFromEnd(head= node1, n = 1)
curr = result
while curr:
    print(curr.val)
    curr = curr.next