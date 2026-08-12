# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:                    # first pass: count nodes
            length += 1
            curr = curr.next

        curr = head
        for _ in range(length // 2):   # second pass: walk to the middle index
            curr = curr.next

        return curr