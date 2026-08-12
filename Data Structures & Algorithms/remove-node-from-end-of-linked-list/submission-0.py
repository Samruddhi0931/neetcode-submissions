# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        curr=head

        while curr:
            length+=1
            curr=curr.next

        target_indx=length - n

        if target_indx==0:
            return head.next

        pre=head
        for i in range(target_indx-1):
            pre=pre.next
        
        temp=pre.next
        pre.next=temp.next
        temp.next=None

        return head


        