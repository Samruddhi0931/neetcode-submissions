# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        before=None
        curr=slow.next
        slow.next=None

        while curr:
            after=curr.next
            curr.next=before
            before=curr
            curr=after

        first,second=head, before
        while second:
            temp1, temp2=first.next,second.next
            first.next= second
            second.next=temp1
            first,second = temp1, temp2


        