# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        
        curr=head
        while curr!=None:
            length+=1
            curr=curr.next
        if length<2:
            head=None
            return head
        curr=head
        prev=None
        count=0
        while curr!=None:
            count+=1
            if count==length//2+1:
                prev.next=curr.next
                curr=prev

            prev=curr
            curr=curr.next
        return head
